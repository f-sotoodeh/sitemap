from datetime import datetime
from flask import Flask, Response, url_for, jsonify
from models import Store, Sale  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
from extensions import db


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)



# This functions  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.get('/robots.txt')
def robots_txt():
    lines = [
        'User-Agent: *',
        'Disallow: /private/',
        'Sitemap: ' + url_for('sitemap', _external=True)
    ]
    return Response('\n'.join(lines), mimetype='text/plain')


@app.get('/sitemap.xml')
def sitemap():
    sitemap_xml = []
    for store in Store.objects:
        store_sitemap_url = url_for('sitemap_store', store_slug=store.slug, _external=True)
        sitemap_xml.append(f'<url><loc>{store_sitemap_url}</loc><lastmod>{datetime.now().date()}</lastmod></url>')
    #
    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?> 
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {''.join(sitemap_xml)}
    </urlset>"""
    return Response(sitemap_content, mimetype='application/xml')


@app.route('/sitemap-store-<store_slug>.xml', methods=['GET'])
def sitemap_store(store_slug):
    sitemap_xml = []
    for sale in Sale.objects(store_slug=store_slug):
        sale_url = f'https://golaabi.com/s/{store_slug}/{sale.slug}'
        sitemap_xml.append(f'<url><loc>{sale_url}</loc><lastmod>{datetime.now().date()}</lastmod></url>')
    #
    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?> 
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {''.join(sitemap_xml)}
    </urlset>"""
    return Response(sitemap_content, mimetype='application/xml')

