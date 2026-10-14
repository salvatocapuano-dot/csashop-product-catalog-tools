import pandas as pd

from csashop_catalog_tools import normalize_catalog


def test_normalize_catalog():
    df = pd.DataFrame(
        {
            "sku": ["A-1", "A-1", "A-2"],
            "title": ["smart bulb", "smart bulb", "smart plug"],
            "brand": ["brand a", "brand a", "brand b"],
            "price": [10.0, 10.0, 20.0],
            "currency": ["EUR", "EUR", "EUR"],
            "stock": [5, 5, 0],
            "image_url": [
                "https://example.com/a.jpg",
                "https://example.com/a.jpg",
                "https://example.com/b.jpg",
            ],
        }
    )

    result = normalize_catalog(df)

    assert len(result) == 2
    assert list(result["availability"]) == ["in_stock", "out_of_stock"]
    assert list(result["title"]) == ["Smart Bulb", "Smart Plug"]
