# 市場與廣告自動化 - n8n 工作流程

## 概覽
本文整理了 n8n 社群工作流程庫中的 **市場與廣告自動化** 工作流程。

**分類：** Marketing & Advertising Automation  
**工作流程總數：** 143  
**產生日期：** 2025-07-27  
**來源：** https://scan-might-updates-postage.trycloudflare.com/api

---

## 工作流程

### Look up a person using their email in Clearbit
**檔名：** `0024_Manual_Clearbit_Send_Triggered.json`  
**描述：** 手動工作流程，整合 Clearbit 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Clearbit,  

---

### Mailcheck Airtable Monitor
**檔名：** `0026_Mailcheck_Airtable_Monitor.json`  
**描述：** 手動工作流程，串接 Airtable 與 Mailcheck for monitoring 與 reporting. 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（4 個節點）  
**整合項目：** Airtable,Mailcheck,  

---

### Manual Ical Send Triggered
**檔名：** `0038_Manual_Ical_Send_Triggered.json`  
**描述：** 手動工作流程，串接 Cal.com 與 Emailsend 以處理資料。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（3 個節點）  
**整合項目：** Cal.com,Emailsend,  

---

### Receive updates when a new account is added by an admin in ActiveCampaign
**檔名：** `0057_Activecampaign_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，整合 Activecampaign 以更新既有資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（1 個節點）  
**整合項目：** Activecampaign,  

---

### Create Email Campaign From LinkedIn Post Interactions
**檔名：** `0090_Wait_Lemlist_Create_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Hubspot, Airtable，以及 Lemlist 以建立新紀錄。 Uses 16 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（16 個節點）  
**整合項目：** Hubspot,Airtable,Lemlist,LinkedIn,Dropcontact,Phantombuster,  

---

### Create a user profile in Vero
**檔名：** `0111_Manual_Vero_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Vero 以建立新紀錄。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Vero,  

---

### Get information about a company with UpLead
**檔名：** `0117_Manual_Uplead_Import_Triggered.json`  
**描述：** 手動工作流程，整合 Uplead 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Uplead,  

---

### Receive messages for an ActiveMQ queue via AMQP Trigger
**檔名：** `0138_Amqp_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，整合 Amqp 以處理資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（1 個節點）  
**整合項目：** Amqp,  

---

### Manual Send Triggered
**檔名：** `0145_Manual_Send_Triggered.json`  
**描述：** 手動工作流程，用於資料處理。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（3 個節點）  
**整合項目：** None  

---

### Receive updates when a form is submitted in Mautic, and send a confirmation SMS
**檔名：** `0155_Mautic_Twilio_Update_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Twilio 與 Mautic 以更新既有資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（2 個節點）  
**整合項目：** Twilio,Mautic,  

---

### Create, update and get a user from Iterable
**檔名：** `0208_Manual_Iterable_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Iterable 以建立新紀錄。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（4 個節點）  
**整合項目：** Iterable,  

---

### Receive messages from a topic and send an SMS
**檔名：** `0209_Noop_Kafka_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Kafka 與 Vonage 以處理資料。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（4 個節點）  
**整合項目：** Kafka,Vonage,  

---

### Create a short URL and get the statistics of the URL
**檔名：** `0210_Manual_Yourls_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Yourls 以建立新紀錄。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（3 個節點）  
**整合項目：** Yourls,  

---

### Mautic Mondaycom Create Triggered
**檔名：** `0275_Mautic_Mondaycom_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Monday.com 與 Mautic 以建立新紀錄。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（3 個節點）  
**整合項目：** Monday.com,Mautic,  

---

### Calendly Mautic Create Triggered
**檔名：** `0277_Calendly_Mautic_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Calendly 與 Mautic 以建立新紀錄。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（3 個節點）  
**整合項目：** Calendly,Mautic,  

---

### Lemlist Slack Create Webhook
**檔名：** `0283_Lemlist_Slack_Create_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Hubspot, OpenAI，以及 Lemlist 以建立新紀錄。 Uses 12 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（12 個節點）  
**整合項目：** Hubspot,OpenAI,Lemlist,Httprequest,Slack,  

---

### Code Readpdf Send Triggered
**檔名：** `0298_Code_Readpdf_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Gmail, OpenAI，以及 Google Drive 以處理資料。 Uses 18 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（18 個節點）  
**整合項目：** Gmail,OpenAI,Google Drive,Readpdf,  

---

### Send Triggered
**檔名：** `0320_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 OpenAI, Agent，以及 Chat 以處理資料。 Uses 5 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（5 個節點）  
**整合項目：** OpenAI,Agent,Chat,Memorybufferwindow,Toolserpapi,  

---

### Splitout Code Send Triggered
**檔名：** `0322_Splitout_Code_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Splitout，以及 Agent 以處理資料。 Uses 18 nodes 與 integrates with 10 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（18 個節點）  
**整合項目：** OpenAI,Splitout,Agent,Gmail,Informationextractor,Documentdefaultdataloader,Textsplitterrecursivecharactertextsplitter,Form Trigger,Toolwikipedia,Chainsummarization,  

---

### Stickynote Send Triggered
**檔名：** `0325_Stickynote_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 OpenAI, Agent，以及 Chat 以處理資料。 Uses 9 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（9 個節點）  
**整合項目：** OpenAI,Agent,Chat,Toolwikipedia,Memorybufferwindow,Toolserpapi,  

---

### Manual Stickynote Send Triggered
**檔名：** `0326_Manual_Stickynote_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Google Drive，以及 Agent 以處理資料。 Uses 15 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（15 個節點）  
**整合項目：** OpenAI,Google Drive,Agent,Vectorstorepinecone,Documentdefaultdataloader,Chat,Textsplitterrecursivecharactertextsplitter,  

---

### Manual Send Triggered
**檔名：** `0329_Manual_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Toolcode, Agent，以及 OpenAI 以處理資料。 Uses 6 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（6 個節點）  
**整合項目：** Toolcode,Agent,OpenAI,Chat,  

---

### Wait Webhook Send Webhook
**檔名：** `0330_Wait_Webhook_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Form Trigger, Webhook，以及 Gmail 以處理資料。 Uses 29 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（29 個節點）  
**整合項目：** Form Trigger,Webhook,Gmail,Httprequest,Itemlists,Slack,  

---

### Stopanderror Extractfromfile Send Webhook
**檔名：** `0331_Stopanderror_Extractfromfile_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Extractfromfile，以及 Html 以處理資料。 Uses 24 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（24 個節點）  
**整合項目：** OpenAI,Extractfromfile,Html,Emailsend,Httprequest,Form Trigger,  

---

### Stickynote Send Triggered
**檔名：** `0332_Stickynote_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Chainllm, Lmopenhuggingfaceinference，以及 Chat 以處理資料。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（4 個節點）  
**整合項目：** Chainllm,Lmopenhuggingfaceinference,Chat,  

---

### Create entry in Mailchimp from Airtable
**檔名：** `0345_Mailchimp_Cron_Create_Scheduled.json`  
**描述：** 排程式自動化流程，串接 Airtable 與 Mailchimp 以建立新紀錄。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 低（3 個節點）  
**整合項目：** Airtable,Mailchimp,  

---

### Send a message on Twake
**檔名：** `0355_Manual_Twake_Send_Triggered.json`  
**描述：** 手動工作流程，整合 Twake 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Twake,  

---

### Email form
**檔名：** `0361_Hunter_Noop_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Sendgrid, Hunter，以及 Form Trigger 以處理資料。 使用 7 個節點。  
**狀態：** 啟用  
**觸發方式：** Webhook  
**複雜度：** 中（7 個節點）  
**整合項目：** Sendgrid,Hunter,Form Trigger,  

---

### Code Manual Send Webhook
**檔名：** `0365_Code_Manual_Send_Webhook.json`  
**描述：** 手動工作流程，串接 Httprequest 與 Google Sheets 以處理資料。 使用 8 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 中（8 個節點）  
**整合項目：** Httprequest,Google Sheets,  

---

### Code Manual Send Webhook
**檔名：** `0367_Code_Manual_Send_Webhook.json`  
**描述：** 手動工作流程，串接 Httprequest 與 Google Sheets 以處理資料。 使用 8 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 中（8 個節點）  
**整合項目：** Httprequest,Google Sheets,  

---

### Manual Stickynote Send Webhook
**檔名：** `0374_Manual_Stickynote_Send_Webhook.json`  
**描述：** 手動工作流程，協調 Httprequest, Box，以及 Form Trigger 以處理資料。 使用 7 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 中（7 個節點）  
**整合項目：** Httprequest,Box,Form Trigger,  

---

### Webhook Code Send Webhook
**檔名：** `0375_Webhook_Code_Send_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Httprequest, Respondtowebhook，以及 Form Trigger 以處理資料。 使用 10 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（10 個節點）  
**整合項目：** Httprequest,Respondtowebhook,Form Trigger,  

---

### Wait Code Send Scheduled
**檔名：** `0385_Wait_Code_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Httprequest, Gmail，以及 Htmlextract 以處理資料。 Uses 15 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（15 個節點）  
**整合項目：** Httprequest,Gmail,Htmlextract,Itemlists,  

---

### Code Filter Send Triggered
**檔名：** `0401_Code_Filter_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Google Sheets，以及 Agent 以處理資料。 Uses 20 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（20 個節點）  
**整合項目：** OpenAI,Google Sheets,Agent,Toolworkflow,Chat,Executeworkflow,Memorybufferwindow,  

---

### Stickynote Send Triggered
**檔名：** `0407_Stickynote_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Cal.com, Memorybufferwindow，以及 OpenAI 以處理資料。 Uses 6 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（6 個節點）  
**整合項目：** Cal.com,Memorybufferwindow,OpenAI,Chat,  

---

### Create, update and get a contact using the SendGrid node
**檔名：** `0408_Manual_Sendgrid_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Sendgrid 以建立新紀錄。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（4 個節點）  
**整合項目：** Sendgrid,  

---

### Filter Form Send Triggered
**檔名：** `0411_Filter_Form_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Clearbit, Gmail，以及 Form Trigger 以處理資料。 使用 13 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（13 個節點）  
**整合項目：** Clearbit,Gmail,Form Trigger,  

---

### Hunter Form Create Triggered
**檔名：** `0420_Hunter_Form_Create_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Hubspot, Clearbit，以及 Hunter 以建立新紀錄。 Uses 11 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（11 個節點）  
**整合項目：** Hubspot,Clearbit,Hunter,Form Trigger,  

---

### Hunter Form Send Webhook
**檔名：** `0424_Hunter_Form_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Httprequest, Gmail，以及 Hunter 以處理資料。 Uses 12 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（12 個節點）  
**整合項目：** Httprequest,Gmail,Hunter,Form Trigger,  

---

### Hunter Form Send Webhook
**檔名：** `0426_Hunter_Form_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Hubspot, Hunter，以及 Gmail 以處理資料。 Uses 15 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（15 個節點）  
**整合項目：** Hubspot,Hunter,Gmail,Httprequest,Form Trigger,  

---

### Filter Convertkit Create Triggered
**檔名：** `0431_Filter_Convertkit_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Hubspot, Clearbit，以及 Convertkit 以建立新紀錄。 使用 16 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 高（16 個節點）  
**整合項目：** Hubspot,Clearbit,Convertkit,  

---

### Hunter Pipedrive Create Triggered
**檔名：** `0436_Hunter_Pipedrive_Create_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Clearbit, Hunter，以及 Pipedrive 以建立新紀錄。 Uses 15 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（15 個節點）  
**整合項目：** Clearbit,Hunter,Pipedrive,Form Trigger,  

---

### Splitout Schedule Send Scheduled
**檔名：** `0442_Splitout_Schedule_Send_Scheduled.json`  
**描述：** 排程式自動化流程，協調 Splitinbatches, Splitout，以及 Gmail 以處理資料。 Uses 10 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 中（10 個節點）  
**整合項目：** Splitinbatches,Splitout,Gmail,Rssfeedread,  

---

### Wait Filter Send Webhook
**檔名：** `0466_Wait_Filter_Send_Webhook.json`  
**描述：** 手動工作流程，串接 Httprequest 與 Google Drive 以處理資料。 使用 14 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 中（14 個節點）  
**整合項目：** Httprequest,Google Drive,  

---

### Webhook Respondtowebhook Send Webhook
**檔名：** `0467_Webhook_Respondtowebhook_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Google Drive，以及 Webhook 以處理資料。 Uses 17 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（17 個節點）  
**整合項目：** OpenAI,Google Drive,Webhook,Chainretrievalqa,Documentdefaultdataloader,Vectorstoreqdrant,Textsplitterrecursivecharactertextsplitter,Chat,Retrievervectorstore,  

---

### Unsubscribe Mautic contacts from automated unsubscribe emails
**檔名：** `0490_Mautic_Gmail_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Server-Sent Events, Gmail，以及 Mautic 以處理資料。 使用 16 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 高（16 個節點）  
**整合項目：** Server-Sent Events,Gmail,Mautic,  

---

### Splitout Schedule Send Scheduled
**檔名：** `0500_Splitout_Schedule_Send_Scheduled.json`  
**描述：** 排程式自動化流程，協調 Markdown, GitHub，以及 Splitout 以處理資料。 Uses 7 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 中（7 個節點）  
**整合項目：** Markdown,GitHub,Splitout,Gmail,  

---

### Manual Extractfromfile Send Webhook
**檔名：** `0501_Manual_Extractfromfile_Send_Webhook.json`  
**描述：** 手動工作流程，串接 Httprequest 與 Extractfromfile 以處理資料。 使用 10 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 中（10 個節點）  
**整合項目：** Httprequest,Extractfromfile,  

---

### Lemlist Slack Create Webhook
**檔名：** `0504_Lemlist_Slack_Create_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Lemlist，以及 Outputparserstructured 以建立新紀錄。 Uses 18 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（18 個節點）  
**整合項目：** OpenAI,Lemlist,Outputparserstructured,Httprequest,Chainllm,Form Trigger,Slack,  

---

### Localfile Splitout Send Triggered
**檔名：** `0536_Localfile_Splitout_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Readwritefile, OpenAI，以及 Splitout 以處理資料。 Uses 17 nodes 與 integrates with 8 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（17 個節點）  
**整合項目：** Readwritefile,OpenAI,Splitout,Agent,Extractfromfile,Outputparserstructured,Localfile,Toolcode,  

---

### Wait Splitout Send Webhook
**檔名：** `0538_Wait_Splitout_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, OpenAI，以及 Compression 以處理資料。 Uses 38 nodes 與 integrates with 15 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（38 個節點）  
**整合項目：** Splitinbatches,OpenAI,Compression,Splitout,Embeddingsmistralcloud,Extractfromfile,Agent,Toolworkflow,Httprequest,Documentdefaultdataloader,Vectorstoreqdrant,Textsplitterrecursivecharactertextsplitter,Chat,Executeworkflow,Memorybufferwindow,  

---

### Code Schedule Send Scheduled
**檔名：** `0553_Code_Schedule_Send_Scheduled.json`  
**描述：** 排程式自動化流程，協調 Ftp, Converttofile，以及 Mqtt 以處理資料。 使用 6 個節點。  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 中（6 個節點）  
**整合項目：** Ftp,Converttofile,Mqtt,  

---

### Code Webhook Send Webhook
**檔名：** `0571_Code_Webhook_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Airtable, Webhook，以及 Gmail 以處理資料。 Uses 13 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（13 個節點）  
**整合項目：** Airtable,Webhook,Gmail,Html,  

---

### Filter Schedule Send Scheduled
**檔名：** `0572_Filter_Schedule_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Notion, Html，以及 Emailsend 以處理資料。 Uses 27 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（27 個節點）  
**整合項目：** Notion,Html,Emailsend,Pushover,  

---

### Stickynote Notion Send Webhook
**檔名：** `0573_Stickynote_Notion_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Toolhttprequest, OpenAI，以及 Agent 以處理資料。 Uses 12 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（12 個節點）  
**整合項目：** Toolhttprequest,OpenAI,Agent,Chat,Form Trigger,Notion,Memorybufferwindow,  

---

### Splitout Filter Send Webhook
**檔名：** `0587_Splitout_Filter_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Splitout，以及 Email (IMAP) 以處理資料。 Uses 11 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（11 個節點）  
**整合項目：** OpenAI,Splitout,Email (IMAP),Httprequest,Box,  

---

### Respondtowebhook Stickynote Send Webhook
**檔名：** `0590_Respondtowebhook_Stickynote_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Toolhttprequest, OpenAI，以及 Webhook 以處理資料。 Uses 28 nodes 與 integrates with 10 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（28 個節點）  
**整合項目：** Toolhttprequest,OpenAI,Webhook,Agent,Toolworkflow,Chat,Form Trigger,Cal.com,Notion,Memorybufferwindow,  

---

### Filter Manual Send Triggered
**檔名：** `0595_Filter_Manual_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, Splitinbatches，以及 Agent 以處理資料。 Uses 36 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（36 個節點）  
**整合項目：** Markdown,Splitinbatches,Agent,Outlook,Lmchatollama,  

---

### Wait Splitout Send Webhook
**檔名：** `0602_Wait_Splitout_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Lmchatgooglegemini, Splitout，以及 Agent 以處理資料。 Uses 35 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（35 個節點）  
**整合項目：** Lmchatgooglegemini,Splitout,Agent,Httprequest,Chainllm,WhatsApp,Form Trigger,Toolwikipedia,Memorybufferwindow,  

---

### Google Maps Email Scraper Template
**檔名：** `0639_Wait_Splitout_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, Splitout，以及 Google Sheets 以處理資料。 Uses 26 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（26 個節點）  
**整合項目：** Splitinbatches,Splitout,Google Sheets,Httprequest,Removeduplicates,Executeworkflow,  

---

### Add subscriber to form, create tag and subscriber to the tag
**檔名：** `0653_Manual_Convertkit_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Convertkit 以建立新紀錄。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（4 個節點）  
**整合項目：** Convertkit,  

---

### Stickynote Respondtowebhook Send Webhook
**檔名：** `0684_Stickynote_Respondtowebhook_Send_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Webhook, Respondtowebhook，以及 Slack 以處理資料。 Uses 10 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（10 個節點）  
**整合項目：** Webhook,Respondtowebhook,Slack,Servicenow,  

---

### Limit Webhook Send Webhook
**檔名：** `0685_Limit_Webhook_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, Webhook，以及 Respondtowebhook 以處理資料。 Uses 29 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（29 個節點）  
**整合項目：** Splitinbatches,Webhook,Respondtowebhook,Httprequest,Servicenow,Form Trigger,Slack,  

---

### Code Respondtowebhook Send Webhook
**檔名：** `0700_Code_Respondtowebhook_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Toolhttprequest, OpenAI，以及 Webhook 以處理資料。 Uses 24 nodes 與 integrates with 11 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（24 個節點）  
**整合項目：** Toolhttprequest,OpenAI,Webhook,Agent,Toolworkflow,Respondtowebhook,Httprequest,Chat,Executeworkflow,Memorybufferwindow,Microsoftoutlook,  

---

### Receive updates when a subscriber is added through a form in ConvertKit
**檔名：** `0723_Convertkit_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，整合 Convertkit 以更新既有資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（1 個節點）  
**整合項目：** Convertkit,  

---

### Schedule Stickynote Send Scheduled
**檔名：** `0729_Schedule_Stickynote_Send_Scheduled.json`  
**描述：** 排程式自動化流程，串接 Ssh 與 Emailsend 以處理資料。 使用 10 個節點。  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 中（10 個節點）  
**整合項目：** Ssh,Emailsend,  

---

### Splitout Noop Send Triggered
**檔名：** `0730_Splitout_Noop_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Splitout, Gmail，以及 Google Drive 以處理資料。 使用 8 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（8 個節點）  
**整合項目：** Splitout,Gmail,Google Drive,  

---

### Receive updates when a subscriber unsubscribes in Customer.io
**檔名：** `0738_Customerio_Update_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，整合 Customerio 以更新既有資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（1 個節點）  
**整合項目：** Customerio,  

---

### SIGNL4 Alert
**檔名：** `0749_Readbinaryfile_Movebinarydata_Send_Scheduled.json`  
**描述：** 排程式自動化流程，協調 Readbinaryfile, Signl4，以及 Writebinaryfile for notifications 與 alerts. Uses 9 nodes 與 integrates with 4 services.  
**狀態：** 啟用  
**觸發方式：** 排程  
**複雜度：** 中（9 個節點）  
**整合項目：** Readbinaryfile,Signl4,Writebinaryfile,Movebinarydata,  

---

### Stickynote Send Webhook
**檔名：** `0755_Stickynote_Send_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Toolhttprequest, OpenAI，以及 Agent 以處理資料。 Uses 6 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（6 個節點）  
**整合項目：** Toolhttprequest,OpenAI,Agent,Toolworkflow,Chat,  

---

### Splitout Code Send Webhook
**檔名：** `0760_Splitout_Code_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Salesforce, Httprequest，以及 Executeworkflow 以處理資料。 Uses 23 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（23 個節點）  
**整合項目：** Salesforce,Httprequest,Executeworkflow,Cal.com,Notion,  

---

### Code Filter Send Webhook
**檔名：** `0767_Code_Filter_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Googlesheetstool, OpenAI，以及 Agent 以處理資料。 Uses 30 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（30 個節點）  
**整合項目：** Googlesheetstool,OpenAI,Agent,Toolworkflow,Httprequest,Chat,Executeworkflow,Cal.com,Memorybufferwindow,  

---

### Receive updates when a subscriber is added to a group and strore the information in Airtable
**檔名：** `0776_Manual_Mailerlite_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Airtable 與 Mailerlite 以更新既有資料。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（4 個節點）  
**整合項目：** Airtable,Mailerlite,  

---

### Splitout Code Send Triggered
**檔名：** `0793_Splitout_Code_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Google Sheets, Gmail，以及 Splitout 以處理資料。 Uses 18 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（18 個節點）  
**整合項目：** Google Sheets,Gmail,Splitout,Form Trigger,  

---

### Schedule Mailchimp Create Scheduled
**檔名：** `0795_Schedule_Mailchimp_Create_Scheduled.json`  
**描述：** 排程式自動化流程，協調 Splitinbatches, Google Sheets，以及 Mailchimp 以建立新紀錄。 使用 6 個節點。  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 中（6 個節點）  
**整合項目：** Splitinbatches,Google Sheets,Mailchimp,  

---

### Create a customer and add them to a segment in Customer.io
**檔名：** `0803_Manual_Customerio_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Customerio 以建立新紀錄。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（3 個節點）  
**整合項目：** Customerio,  

---

### Send Triggered
**檔名：** `0804_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Agent, OpenAI，以及 Chat 以處理資料。 使用 5 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（5 個節點）  
**整合項目：** Agent,OpenAI,Chat,  

---

### Code Form Send Webhook
**檔名：** `0808_Code_Form_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Agent，以及 Gmail 以處理資料。 Uses 19 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（19 個節點）  
**整合項目：** OpenAI,Agent,Gmail,Httprequest,Form Trigger,  

---

### Wait Code Send Webhook
**檔名：** `0820_Wait_Code_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, Splitinbatches，以及 Lmchatgooglegemini 以處理資料。 Uses 24 nodes 與 integrates with 8 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（24 個節點）  
**整合項目：** Markdown,Splitinbatches,Lmchatgooglegemini,Microsoftexcel,Extractfromfile,Httprequest,Textclassifier,Microsoftoutlook,  

---

### Filter Summarize Send Scheduled
**檔名：** `0830_Filter_Summarize_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Googlesheetstool, Google Sheets，以及 Gmail 以處理資料。 Uses 20 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（20 個節點）  
**整合項目：** Googlesheetstool,Google Sheets,Gmail,Extractfromfile,Informationextractor,Form Trigger,Cal.com,  

---

### Splitout Limit Send Webhook
**檔名：** `0860_Splitout_Limit_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Vectorstoremilvus，以及 Splitout 以處理資料。 Uses 22 nodes 與 integrates with 10 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（22 個節點）  
**整合項目：** OpenAI,Vectorstoremilvus,Splitout,Chainretrievalqa,Html,Httprequest,Documentdefaultdataloader,Chat,Textsplitterrecursivecharactertextsplitter,Retrievervectorstore,  

---

### Wait Datetime Send Scheduled
**檔名：** `0869_Wait_Datetime_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, Datetime，以及 Toolthink 以處理資料。 Uses 30 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（30 個節點）  
**整合項目：** Splitinbatches,Datetime,Toolthink,Lmchatgooglegemini,Html,Outlook,MySQL,Form Trigger,Cal.com,  

---

### Wait Code Send Webhook
**檔名：** `0888_Wait_Code_Send_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Httprequest, Webhook，以及 Emailsend 以處理資料。 使用 15 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（15 個節點）  
**整合項目：** Httprequest,Webhook,Emailsend,  

---

### Form Stickynote Send Triggered
**檔名：** `0890_Form_Stickynote_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Hubspot, OpenAI，以及 Agent 以處理資料。 Uses 14 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（14 個節點）  
**整合項目：** Hubspot,OpenAI,Agent,Gmail,Form Trigger,Chainsummarization,  

---

### Limit Code Send Scheduled
**檔名：** `0897_Limit_Code_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, Discord，以及 Google Drive 以處理資料。 Uses 29 nodes 與 integrates with 8 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（29 個節點）  
**整合項目：** Splitinbatches,Discord,Google Drive,Gmail,Executiondata,Server-Sent Events,N8N,Executeworkflow,  

---

### Bitly Datetime Update Webhook
**檔名：** `0910_Bitly_Datetime_Update_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Twitter/X, Dropbox，以及 Toolhttprequest 以更新既有資料。 Uses 113 nodes 與 integrates with 61 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（113 個節點）  
**整合項目：** Twitter/X,Dropbox,Toolhttprequest,Vectorstoreinmemory,Converttofile,Google Drive,Splitinbatches,Rssfeedread,Google Sheets,Webhook,Chainretrievalqa,Executiondata,Bitly,Emailsendtool,Removeduplicates,Pushbullet,Cal.com,Toolcode,Gumroad,Google Calendar,Markdown,Memorymanager,Datetime,Executecommand,OpenAI,Toolwolframalpha,Email (IMAP),Vectorstoresupabase,Anthropic,Httprequest,Renamekeys,Form Trigger,Mcpclienttool,Chainsummarization,Executeworkflow,Lmchatgooglegemini,Splitout,Agent,Gmail,Vectorstorepinecone,Outputparseritemlist,Outputparserstructured,PostgreSQL,Chainllm,Reddit,Documentdefaultdataloader,Chat,Toolwikipedia,Sentimentanalysis,Redis,Textclassifier,Toolserpapi,Ftp,Google Docs,Extractfromfile,Html,Outputparserautofixing,Youtube,Embeddingsgooglegemini,Memorybufferwindow,Toolvectorstore,  

---

### Code Noop Send Triggered
**檔名：** `0918_Code_Noop_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, OpenAI，以及 Google Sheets 以處理資料。 Uses 19 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（19 個節點）  
**整合項目：** Splitinbatches,OpenAI,Google Sheets,Agent,Chat,Form Trigger,Executeworkflow,Cal.com,Memorybufferwindow,  

---

### Splitout Code Send Scheduled
**檔名：** `0921_Splitout_Code_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, Lmchatgooglegemini，以及 Splitout 以處理資料。 Uses 47 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（47 個節點）  
**整合項目：** Splitinbatches,Lmchatgooglegemini,Splitout,Chainllm,Executeworkflow,Slack,  

---

### Splitout Code Send Scheduled
**檔名：** `0923_Splitout_Code_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, OpenAI，以及 Microsoftteams 以處理資料。 Uses 17 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（17 個節點）  
**整合項目：** Markdown,OpenAI,Microsoftteams,Splitout,Chainllm,  

---

### Mailchimp
**檔名：** `0938_Manual_Mailchimp_Automation_Triggered.json`  
**描述：** 手動工作流程，整合 Mailchimp 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Mailchimp,  

---

### Analyze_email_headers_for_IPs_and_spoofing__3
**檔名：** `0946_Code_Webhook_Send_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Httprequest, Webhook，以及 Itemlists 以處理資料。 使用 35 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 高（35 個節點）  
**整合項目：** Httprequest,Webhook,Itemlists,  

---

### Manual Activecampaign Automation Triggered
**檔名：** `0951_Manual_Activecampaign_Automation_Triggered.json`  
**描述：** 手動工作流程，整合 Activecampaign 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Activecampaign,  

---

### Mautic Webhook Update Webhook
**檔名：** `0963_Mautic_Webhook_Update_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Webhook 與 Mautic 以更新既有資料。 使用 17 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 高（17 個節點）  
**整合項目：** Webhook,Mautic,  

---

### Manual Awsses Automate Triggered
**檔名：** `0983_Manual_Awsses_Automate_Triggered.json`  
**描述：** 手動工作流程，整合 Awsses 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Awsses,  

---

### Send an SMS using MSG91
**檔名：** `0986_Manual_Msg91_Send_Triggered.json`  
**描述：** 手動工作流程，整合 Msg91 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Msg91,  

---

### Mailchimp Automate Triggered
**檔名：** `0989_Mailchimp_Automate_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，整合 Mailchimp 以處理資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（1 個節點）  
**整合項目：** Mailchimp,  

---

### Manual Hunter Automate Triggered
**檔名：** `0991_Manual_Hunter_Automate_Triggered.json`  
**描述：** 手動工作流程，整合 Hunter 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Hunter,  

---

### Manual Mailjet Automate Triggered
**檔名：** `0993_Manual_Mailjet_Automate_Triggered.json`  
**描述：** 手動工作流程，整合 Mailjet 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Mailjet,  

---

### Mailjet Automate Triggered
**檔名：** `0994_Mailjet_Automate_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，整合 Mailjet 以處理資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（1 個節點）  
**整合項目：** Mailjet,  

---

### Manual Mautic Automate Triggered
**檔名：** `1017_Manual_Mautic_Automate_Triggered.json`  
**描述：** 手動工作流程，整合 Mautic 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Mautic,  

---

### Manual Mandrill Automate Triggered
**檔名：** `1037_Manual_Mandrill_Automate_Triggered.json`  
**描述：** 手動工作流程，整合 Mandrill 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Mandrill,  

---

### Manual Emailsend Send Triggered
**檔名：** `1047_Manual_Emailsend_Send_Triggered.json`  
**描述：** 手動工作流程，整合 Emailsend 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Emailsend,  

---

### Emailreadimap Send
**檔名：** `1050_Emailreadimap_Send.json`  
**描述：** 手動工作流程，整合 Email (IMAP) 以處理資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（1 個節點）  
**整合項目：** Email (IMAP),  

---

### Mautic Googlesheets Automate Scheduled
**檔名：** `1083_Mautic_GoogleSheets_Automate_Scheduled.json`  
**描述：** 排程式自動化流程，串接 Google Sheets 與 Mautic 以處理資料。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 低（4 個節點）  
**整合項目：** Google Sheets,Mautic,  

---

### Sse Automation Triggered
**檔名：** `1084_Sse_Automation_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，整合 Server-Sent Events 以處理資料。 使用 1 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（1 個節點）  
**整合項目：** Server-Sent Events,  

---

### Create a new list, add a new contact to the list, update the contact, and get all contacts in the list
**檔名：** `1154_Manual_Automizy_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Automizy 以建立新紀錄。 使用 5 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（5 個節點）  
**整合項目：** Automizy,  

---

### New WooCommerce Customer to Mautic
**檔名：** `1160_Mautic_Woocommerce_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Mautic 與 Woocommerce 以處理資料。 使用 5 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（5 個節點）  
**整合項目：** Mautic,Woocommerce,  

---

### Check for valid Mautic contact email
**檔名：** `1168_Mautic_Slack_Send_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Onesimpleapi, Slack，以及 Mautic 以處理資料。 Uses 6 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（6 個節點）  
**整合項目：** Onesimpleapi,Slack,Mautic,Form Trigger,  

---

### Sending an SMS using sms77
**檔名：** `1199_Manual_Sms77_Send_Triggered.json`  
**描述：** 手動工作流程，整合 Sms77 以處理資料。 使用 2 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（2 個節點）  
**整合項目：** Sms77,  

---

### Getresponse Airtable Import Triggered
**檔名：** `1202_Getresponse_Airtable_Import_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Airtable 與 Getresponse 以處理資料。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（3 個節點）  
**整合項目：** Airtable,Getresponse,  

---

### Manual Tapfiliate Automate Triggered
**檔名：** `1205_Manual_Tapfiliate_Automate_Triggered.json`  
**描述：** 手動工作流程，整合 Tapfiliate 以處理資料。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（4 個節點）  
**整合項目：** Tapfiliate,  

---

### Emelia Automate
**檔名：** `1214_Emelia_Automate.json`  
**描述：** 手動工作流程，整合 Emelia 以處理資料。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（3 個節點）  
**整合項目：** Emelia,  

---

### Create, update and get a subscriber using the MailerLite node
**檔名：** `1218_Manual_Mailerlite_Create_Triggered.json`  
**描述：** 手動工作流程，整合 Mailerlite 以建立新紀錄。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（4 個節點）  
**整合項目：** Mailerlite,  

---

### Autopilot Automate
**檔名：** `1227_Autopilot_Automate.json`  
**描述：** 手動工作流程，整合 Autopilot 以處理資料。 使用 4 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（4 個節點）  
**整合項目：** Autopilot,  

---

### Autopilot Airtable Automate Triggered
**檔名：** `1228_Autopilot_Airtable_Automate_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Airtable 與 Autopilot 以處理資料。 使用 3 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 低（3 個節點）  
**整合項目：** Airtable,Autopilot,  

---

### Very simple Human in the loop system email with AI e IMAP
**檔名：** `1240_Markdown_Stickynote_Send.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, OpenAI，以及 Email (IMAP) 以處理資料。 Uses 16 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（16 個節點）  
**整合項目：** Markdown,OpenAI,Email (IMAP),Agent,Emailsend,Chainsummarization,  

---

### Email AI Auto-responder. Summerize and send email
**檔名：** `1277_Emailreadimap_Manual_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, Textsplittertokensplitter，以及 OpenAI 以處理資料。 Uses 26 nodes 與 integrates with 14 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（26 個節點）  
**整合項目：** Markdown,Textsplittertokensplitter,OpenAI,Google Drive,Lmchatopenai,Email (IMAP),Agent,Emailsend,Httprequest,Chainllm,Vectorstoreqdrant,Documentdefaultdataloader,Chainsummarization,Textclassifier,  

---

### AI Email processing autoresponder with approval (Yes/No)
**檔名：** `1284_Emailreadimap_Markdown_Send.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, OpenAI，以及 Lmchatopenai 以處理資料。 Uses 17 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（17 個節點）  
**整合項目：** Markdown,OpenAI,Lmchatopenai,Email (IMAP),Agent,Gmail,Emailsend,Vectorstoreqdrant,Chainsummarization,  

---

### Code Converttofile Send Webhook
**檔名：** `1307_Code_Converttofile_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Converttofile, OpenAI，以及 Gmail 以處理資料。 Uses 25 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（25 個節點）  
**整合項目：** Converttofile,OpenAI,Gmail,Jira,Httprequest,Outlook,Form Trigger,  

---

### Filter Manual Send Triggered
**檔名：** `1321_Filter_Manual_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, Splitinbatches，以及 Agent 以處理資料。 Uses 36 nodes 與 integrates with 5 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（36 個節點）  
**整合項目：** Markdown,Splitinbatches,Agent,Outlook,Lmchatollama,  

---

### Lemlist Slack Automate Webhook
**檔名：** `1382_Lemlist_Slack_Automate_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 OpenAI, Lemlist，以及 Outputparserstructured 以處理資料。 Uses 18 nodes 與 integrates with 7 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（18 個節點）  
**整合項目：** OpenAI,Lemlist,Outputparserstructured,Httprequest,Chainllm,Form Trigger,Slack,  

---

### Send Emails from Obsidian
**檔名：** `1403_Splitout_Datetime_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Splitinbatches, Converttofile，以及 Datetime 以處理資料。 Uses 19 nodes 與 integrates with 7 services.  
**狀態：** 啟用  
**觸發方式：** 複雜  
**複雜度：** 高（19 個節點）  
**整合項目：** Splitinbatches,Converttofile,Datetime,Splitout,Respondtowebhook,Gmail,Webhook,  

---

### Effortless Email Management with AI
**檔名：** `1427_Emailreadimap_Manual_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, Textsplittertokensplitter，以及 OpenAI 以處理資料。 Uses 31 nodes 與 integrates with 14 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（31 個節點）  
**整合項目：** Markdown,Textsplittertokensplitter,OpenAI,Google Drive,Email (IMAP),Agent,Gmail,Emailsend,Httprequest,Lmchatdeepseek,Documentdefaultdataloader,Vectorstoreqdrant,Chainsummarization,Textclassifier,  

---

### Code Schedule Send Scheduled
**檔名：** `1428_Code_Schedule_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Editimage, OpenAI，以及 Lmchatgroq 以處理資料。 Uses 32 nodes 與 integrates with 11 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（32 個節點）  
**整合項目：** Editimage,OpenAI,Lmchatgroq,Airtable,Agent,Gmail,Executiondata,Form Trigger,Executeworkflow,Toolwikipedia,Memorybufferwindow,  

---

### Code Schedule Send Scheduled
**檔名：** `1429_Code_Schedule_Send_Scheduled.json`  
**描述：** 複雜的多步驟自動化流程，協調 Editimage, OpenAI，以及 Lmchatgroq 以處理資料。 Uses 32 nodes 與 integrates with 11 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（32 個節點）  
**整合項目：** Editimage,OpenAI,Lmchatgroq,Airtable,Agent,Gmail,Executiondata,Form Trigger,Executeworkflow,Toolwikipedia,Memorybufferwindow,  

---

### Email Summary Agent
**檔名：** `1430_Aggregate_Schedule_Send_Scheduled.json`  
**描述：** 排程式自動化流程，串接 Gmail 與 OpenAI 以處理資料。 使用 9 個節點。  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 中（9 個節點）  
**整合項目：** Gmail,OpenAI,  

---

### [hiroshidigital.com] Send Message In Larksuite
**檔名：** `1505_Manual_Stickynote_Send_Webhook.json`  
**描述：** 手動工作流程，整合 Httprequest 以處理資料。 使用 6 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 中（6 個節點）  
**整合項目：** Httprequest,  

---

### Email verification with Icypeas (single)
**檔名：** `1516_Manual_Stickynote_Send_Webhook.json`  
**描述：** 手動工作流程，整合 Httprequest 以處理資料。 使用 6 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 中（6 個節點）  
**整合項目：** Httprequest,  

---

### Shopify + Mautic
**檔名：** `1526_Mautic_Webhook_Automation_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Shopify, Crypto，以及 GraphQL 以處理資料。 Uses 26 nodes 與 integrates with 5 services.  
**狀態：** 啟用  
**觸發方式：** 複雜  
**複雜度：** 高（26 個節點）  
**整合項目：** Shopify,Crypto,GraphQL,Webhook,Mautic,  

---

### Email Summary Agent
**檔名：** `1544_Aggregate_Schedule_Send_Scheduled.json`  
**描述：** 排程式自動化流程，串接 Gmail 與 OpenAI 以處理資料。 使用 9 個節點。  
**狀態：** 停用  
**觸發方式：** 排程  
**複雜度：** 中（9 個節點）  
**整合項目：** Gmail,OpenAI,  

---

### Very simple Human in the loop system email with AI e IMAP
**檔名：** `1571_Markdown_Stickynote_Send.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, OpenAI，以及 Email (IMAP) 以處理資料。 Uses 16 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（16 個節點）  
**整合項目：** Markdown,OpenAI,Email (IMAP),Agent,Emailsend,Chainsummarization,  

---

### AI Email processing autoresponder with approval (Yes/No)
**檔名：** `1588_Emailreadimap_Markdown_Send.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, OpenAI，以及 Lmchatopenai 以處理資料。 Uses 17 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（17 個節點）  
**整合項目：** Markdown,OpenAI,Lmchatopenai,Email (IMAP),Agent,Gmail,Emailsend,Vectorstoreqdrant,Chainsummarization,  

---

### The Easiest Way to Send SMS Worldwide
**檔名：** `1616_Manual_Stickynote_Send_Webhook.json`  
**描述：** 手動工作流程，整合 Httprequest 以處理資料。 使用 5 個節點。  
**狀態：** 停用  
**觸發方式：** 手動  
**複雜度：** 低（5 個節點）  
**整合項目：** Httprequest,  

---

### Wait Splitout Send Webhook
**檔名：** `1638_Wait_Splitout_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Lmchatgooglegemini, Splitout，以及 Agent 以處理資料。 Uses 35 nodes 與 integrates with 9 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（35 個節點）  
**整合項目：** Lmchatgooglegemini,Splitout,Agent,Httprequest,Chainllm,WhatsApp,Form Trigger,Toolwikipedia,Memorybufferwindow,  

---

### Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV
**檔名：** `1648_Splitout_Converttofile_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Converttofile, Google Sheets，以及 Splitout 以處理資料。 Uses 11 nodes 與 integrates with 6 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 中（11 個節點）  
**整合項目：** Converttofile,Google Sheets,Splitout,Gmail,Html,Httprequest,  

---

### Code Webhook Send Webhook
**檔名：** `1653_Code_Webhook_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Crypto, OpenAI，以及 Google Sheets 以處理資料。 Uses 49 nodes 與 integrates with 8 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（49 個節點）  
**整合項目：** Crypto,OpenAI,Google Sheets,Webhook,Gmail,Html,Respondtowebhook,Form Trigger,  

---

### Code Readpdf Send Triggered
**檔名：** `1656_Code_Readpdf_Send_Triggered.json`  
**描述：** 複雜的多步驟自動化流程，協調 Gmail, OpenAI，以及 Google Drive 以處理資料。 Uses 18 nodes 與 integrates with 4 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（18 個節點）  
**整合項目：** Gmail,OpenAI,Google Drive,Readpdf,  

---

### Gumroad sale trigger
**檔名：** `1874_Mailerlite_Gumroad_Automation_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Httprequest, Gumroad，以及 Google Sheets 以處理資料。 Uses 8 nodes 與 integrates with 4 services.  
**狀態：** 啟用  
**觸發方式：** Webhook  
**複雜度：** 中（8 個節點）  
**整合項目：** Httprequest,Gumroad,Google Sheets,Mailerlite,  

---

### Wordpress Form to Mautic
**檔名：** `1892_Noop_Mautic_Automation_Webhook.json`  
**描述：** 由 Webhook 觸發的自動化流程，串接 Mautic 與 Form Trigger 以處理資料。 使用 10 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（10 個節點）  
**整合項目：** Mautic,Form Trigger,  

---

### Effortless Email Management with AI
**檔名：** `1936_Emailreadimap_Manual_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, Textsplittertokensplitter，以及 OpenAI 以處理資料。 Uses 31 nodes 與 integrates with 14 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（31 個節點）  
**整合項目：** Markdown,Textsplittertokensplitter,OpenAI,Google Drive,Email (IMAP),Agent,Gmail,Emailsend,Httprequest,Lmchatdeepseek,Documentdefaultdataloader,Vectorstoreqdrant,Chainsummarization,Textclassifier,  

---

### Forward Netflix emails to multiple email addresses with GMail and Mailjet
**檔名：** `1956_Mailjet_Gmail_Create_Triggered.json`  
**描述：** 由 Webhook 觸發的自動化流程，協調 Mailjet, Splitout，以及 Gmail 以處理資料。 使用 7 個節點。  
**狀態：** 停用  
**觸發方式：** Webhook  
**複雜度：** 中（7 個節點）  
**整合項目：** Mailjet,Splitout,Gmail,  

---

### Email AI Auto-responder. Summerize and send email
**檔名：** `1962_Emailreadimap_Manual_Send_Webhook.json`  
**描述：** 複雜的多步驟自動化流程，協調 Markdown, Textsplittertokensplitter，以及 OpenAI 以處理資料。 Uses 26 nodes 與 integrates with 14 services.  
**狀態：** 停用  
**觸發方式：** 複雜  
**複雜度：** 高（26 個節點）  
**整合項目：** Markdown,Textsplittertokensplitter,OpenAI,Google Drive,Lmchatopenai,Email (IMAP),Agent,Emailsend,Httprequest,Chainllm,Vectorstoreqdrant,Documentdefaultdataloader,Chainsummarization,Textclassifier,  

---


## 摘要

**市場與廣告自動化工作流程總數：** 143  
**文件產生時間：** 2025-07-27 14:36:56  
**API 來源：** https://scan-might-updates-postage.trycloudflare.com/api  

此文件透過 n8n 工作流程 API 端點自動生成。
