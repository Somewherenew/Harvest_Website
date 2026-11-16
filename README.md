# Harvests Gateway Ltd. Website

A showcase website for Harvests Gateway Ltd. ("Harvests, Freshly Made"), with
WhatsApp ordering on every product.

- **Language:** Python 3.10 or newer
- **Framework:** Flask 3 (Jinja2 templates), plain HTML, CSS and JavaScript
- **Database:** none yet. PostgreSQL will come in with the admin panel.
- **Runs on:** Windows, macOS or Linux

## Run it

```bash
# 1. Open a terminal in this folder (harvests-website)

# 2. Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 3. Install Flask
pip install -r requirements.txt

# 4. Start the site
python run.py
```

Open **http://127.0.0.1:5000** in your browser.

To test it on your phone, connect the phone to the same Wi-Fi and open
`http://<your-computer-ip>:5000`. (On Windows, run `ipconfig` to find the IP address.)

## Pages

| Page | URL | Content |
|------|-----|---------|
| Home | `/` | Hero, "View our snacks" button, featured snacks, welcome message, food safety summary |
| Our Snacks | `/products` | All 7 snacks with category filters and an Order on WhatsApp button on each |
| About Us | `/about` | Story, vision, mission, purpose, values, culture, organisational structure |
| Food Safety | `/quality` | The five food safety and hygiene commitments |
| Contact | `/contact` | WhatsApp, phone, email and a quick order form that opens WhatsApp |

## Editing content

All text, products and contact details are in **`app/content.py`**.

- **WhatsApp number:** `COMPANY["whatsapp"]` (digits only, international format)
- **Add a product:** copy a block in `PRODUCTS`, put its image in
  `app/static/img/products/`, and set `"featured": True` to show it on the Home page
- Text marked `DRAFT` in that file was written for the website and needs approval

## Folder layout

```
harvests-website/
├── run.py                 # start the site
├── config.py              # settings
├── requirements.txt
└── app/
    ├── __init__.py        # app factory and WhatsApp link builder
    ├── routes.py          # page routes
    ├── content.py         # all site text and products
    ├── templates/         # HTML pages (Jinja2)
    └── static/
        ├── css/style.css
        ├── js/main.js
        └── img/           # logo, product and section images
```
