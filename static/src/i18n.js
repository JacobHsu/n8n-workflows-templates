// Simple i18n implementation for N8N Workflow Documentation
const i18n = {
  currentLang: 'zh-TW',

  translations: {
    'zh-TW': {
      'app.title': '⚡ N8N 工作流程文件',
      'header.workflows': '工作流程',
      'header.search': '搜尋',
      'stats.workflows': '個工作流程',
      'stats.categories': '個分類',
      'stats.nodes': '個節點',
      'stats.integrations': '個整合'
    },
    'en': {
      'app.title': '⚡ N8N Workflow Documentation',
      'header.workflows': 'Workflows',
      'header.search': 'Search',
      'stats.workflows': 'workflows',
      'stats.categories': 'categories',
      'stats.nodes': 'nodes',
      'stats.integrations': 'integrations'
    }
  },

  t(key) {
    return this.translations[this.currentLang]?.[key] || key;
  },

  init() {
    // Initialize i18n on page load
    document.addEventListener('DOMContentLoaded', () => {
      this.updateTexts();
    });
  },

  updateTexts() {
    // Update all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
      const key = element.getAttribute('data-i18n');
      const translation = this.t(key);

      if (element.tagName === 'TITLE') {
        element.textContent = translation;
      } else {
        element.textContent = translation;
      }
    });
  },

  setLang(lang) {
    this.currentLang = lang;
    this.updateTexts();
  }
};

// Initialize i18n
i18n.init();

// Make i18n globally available
window.i18n = i18n;