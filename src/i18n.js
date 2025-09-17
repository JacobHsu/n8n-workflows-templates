/**
 * Internationalization (i18n) utility for N8N Workflow Documentation
 * Supports Traditional Chinese (zh-TW) and English (en)
 * Default language: Traditional Chinese (zh-TW)
 */

class I18n {
  constructor() {
    this.currentLanguage = 'zh-TW'; // Default to Traditional Chinese
    this.translations = {};
    this.fallbackLanguage = 'en';
    this.supportedLanguages = ['zh-TW', 'en'];

    // Initialize with browser language or default
    this.init();
  }

  /**
   * Initialize i18n system
   */
  async init() {
    // Get saved language or browser preference, default to zh-TW
    const savedLanguage = localStorage.getItem('language');
    const browserLanguage = this.getBrowserLanguage();

    this.currentLanguage = savedLanguage || browserLanguage || 'zh-TW';

    // Ensure we support the language
    if (!this.supportedLanguages.includes(this.currentLanguage)) {
      this.currentLanguage = 'zh-TW';
    }

    // Load translations
    await this.loadTranslations();

    // Update document language
    document.documentElement.lang = this.currentLanguage;
  }

  /**
   * Get browser language preference
   */
  getBrowserLanguage() {
    const browserLang = navigator.language || navigator.userLanguage;

    // Map browser language codes to our supported languages
    const langMap = {
      'zh-TW': 'zh-TW',
      'zh-tw': 'zh-TW',
      'zh-Hant': 'zh-TW',
      'zh-hant': 'zh-TW',
      'zh': 'zh-TW', // Default Chinese to Traditional
      'en': 'en',
      'en-US': 'en',
      'en-GB': 'en'
    };

    return langMap[browserLang] || langMap[browserLang.split('-')[0]] || 'zh-TW';
  }

  /**
   * Load translation files
   */
  async loadTranslations() {
    try {
      // Load current language
      const currentLangResponse = await fetch(`/locales/${this.currentLanguage}.json`);
      if (currentLangResponse.ok) {
        this.translations[this.currentLanguage] = await currentLangResponse.json();
      }

      // Load fallback language if different
      if (this.currentLanguage !== this.fallbackLanguage) {
        const fallbackResponse = await fetch(`/locales/${this.fallbackLanguage}.json`);
        if (fallbackResponse.ok) {
          this.translations[this.fallbackLanguage] = await fallbackResponse.json();
        }
      }
    } catch (error) {
      console.warn('Failed to load translations:', error);
      // Fallback to built-in translations if fetch fails
      this.loadBuiltinTranslations();
    }
  }

  /**
   * Load built-in translations as fallback
   */
  loadBuiltinTranslations() {
    // Basic built-in translations for critical UI elements
    this.translations['zh-TW'] = {
      app: { title: "⚡ N8N 工作流程文件" },
      search: { placeholder: "搜尋工作流程..." },
      messages: { loading: "載入中..." }
    };

    this.translations['en'] = {
      app: { title: "⚡ N8N Workflow Documentation" },
      search: { placeholder: "Search workflows..." },
      messages: { loading: "Loading..." }
    };
  }

  /**
   * Get translated text by key path
   * @param {string} keyPath - Dot notation key path (e.g., 'app.title')
   * @param {object} interpolations - Values to interpolate (e.g., {count: 5})
   * @returns {string} Translated text
   */
  t(keyPath, interpolations = {}) {
    const keys = keyPath.split('.');
    let translation = this.getNestedValue(this.translations[this.currentLanguage], keys) ||
                     this.getNestedValue(this.translations[this.fallbackLanguage], keys) ||
                     keyPath; // Return key path if no translation found

    // Handle interpolations (e.g., {{count}} -> actual count value)
    if (typeof translation === 'string' && Object.keys(interpolations).length > 0) {
      Object.keys(interpolations).forEach(key => {
        const regex = new RegExp(`{{${key}}}`, 'g');
        translation = translation.replace(regex, interpolations[key]);
      });
    }

    return translation;
  }

  /**
   * Get nested object value by key array
   */
  getNestedValue(obj, keys) {
    return keys.reduce((current, key) => current && current[key], obj);
  }

  /**
   * Set current language
   * @param {string} language - Language code
   */
  async setLanguage(language) {
    if (!this.supportedLanguages.includes(language)) {
      console.warn(`Unsupported language: ${language}`);
      return;
    }

    this.currentLanguage = language;
    localStorage.setItem('language', language);
    document.documentElement.lang = language;

    // Reload translations for new language
    await this.loadTranslations();

    // Emit language change event
    window.dispatchEvent(new CustomEvent('languageChanged', {
      detail: { language }
    }));
  }

  /**
   * Get current language
   */
  getCurrentLanguage() {
    return this.currentLanguage;
  }

  /**
   * Get supported languages
   */
  getSupportedLanguages() {
    return this.supportedLanguages;
  }

  /**
   * Check if language is RTL (Right-to-Left)
   */
  isRTL(language = this.currentLanguage) {
    const rtlLanguages = ['ar', 'he', 'fa', 'ur'];
    return rtlLanguages.includes(language);
  }

  /**
   * Format number according to current locale
   */
  formatNumber(number) {
    const localeMap = {
      'zh-TW': 'zh-TW',
      'en': 'en-US'
    };

    return new Intl.NumberFormat(localeMap[this.currentLanguage] || 'en-US').format(number);
  }

  /**
   * Format date according to current locale
   */
  formatDate(date, options = {}) {
    const localeMap = {
      'zh-TW': 'zh-TW',
      'en': 'en-US'
    };

    const defaultOptions = {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    };

    return new Intl.DateTimeFormat(
      localeMap[this.currentLanguage] || 'en-US',
      { ...defaultOptions, ...options }
    ).format(new Date(date));
  }
}

// Export for both CommonJS and ES modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = I18n;
} else {
  window.I18n = I18n;
}