# CSASHOP Product Catalog Tools

**CSASHOP Product Catalog Tools** is an open-source toolkit for importing, cleaning, normalizing and exporting ecommerce product catalogs.

It helps merchants and developers transform supplier files — CSV, XLSX or JSON — into structured product data ready for Shopify, WooCommerce, custom ecommerce platforms or internal tools.

## Why this project exists

Supplier catalogs are often inconsistent: product titles, brands, SKUs, prices, availability, categories and image URLs use different formats.

This project reduces manual work by providing reusable tools to:

- Import product data from CSV, XLSX and JSON files
- Clean and normalize product titles, brands, SKUs and categories
- Standardize prices, currencies, availability and image URLs
- Detect duplicates and missing required fields
- Export catalogs to clean CSV, JSON or platform-ready formats
- Prepare product data for ecommerce websites, marketplaces and automation workflows

## Features

- Modular Python-based pipeline
- CSV, XLSX and JSON import
- Field mapping and validation
- Product title and brand normalization
- SKU generation and duplicate detection
- Price and availability normalization
- Image URL validation
- Export to CSV and JSON
- Example datasets and configuration files
- Easy integration with ecommerce and automation tools

## Installation

```bash
git clone [https://github.com/YOUR_USERNAME/csashop-product-catalog-tools.git](https://github.com/YOUR_USERNAME/csashop-product-catalog-tools.git)
cd csashop-product-catalog-tools
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Quick start

```bash
python csashop_catalog_tools.py \
  --input examples/sample_products.csv \
  --output output/clean_catalog.csv \
  --format csv
```

Example input:

```csv
sku,title,brand,price,currency,stock,image_url
ABC-001,Smart Wi-Fi Bulb RGB 10W,GenericBrand,19.90,EUR,25,[https://example.com/bulb.jpg](https://example.com/bulb.jpg)
ABC-002,Smart Plug Wi-Fi 16A,GenericBrand,12.50,EUR,40,[https://example.com/plug.jpg](https://example.com/plug.jpg)
```

Example output:

```json
{
  "sku": "ABC-001",
  "title": "Smart Wi-Fi Bulb RGB 10W",
  "brand": "GenericBrand",
  "price": 19.90,
  "currency": "EUR",
  "availability": "in_stock",
  "image_url": "[https://example.com/bulb.jpg](https://example.com/bulb.jpg)"
}
```

## Project structure

```text
csashop-product-catalog-tools/
├── csashop_catalog_tools.py
├── requirements.txt
├── examples/
│   └── sample_products.csv
├── output/
├── tests/
│   └── test_catalog_tools.py
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Roadmap

- [ ] Shopify CSV export
- [ ] WooCommerce product import support
- [ ] Marketplace feed generation
- [ ] AI-assisted product title cleanup
- [ ] Category mapping rules
- [ ] Multi-language product support
- [ ] Web interface
- [ ] Docker support

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

Please add tests for new features and update the documentation when needed.

## License

This project is released under the MIT License.
