from unittest.mock import patch

import pytest
import requests

from source.pricing_module import fetch_product_price, calculate_tax


@pytest.mark.parametrize("product_id, price, expected",[
    (_, 50 * _, 10 * _) for _ in range(1, 100)
])
def test_calculate_tax_with_mocked_api(product_id, price, expected):
    with patch("source.pricing_module.fetch_product_price", return_value=price):
        assert calculate_tax(product_id) == expected

# def test_calculate_tax_if_api_bugs():
#     with patch("pricing_module.fetch_product_price",
#                side_effect=requests.exceptions.RequestException):
#         with pytest.raises(requests.exceptions.RequestException):
#             calculate_tax(1)
