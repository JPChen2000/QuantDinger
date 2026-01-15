"""
Seed symbol list used by Market APIs in local-only mode.

This file is derived from the legacy MySQL `qd_market_symbols` table (non-secret data).
It provides a deterministic offline list for:
- hot symbols per market
- lightweight symbol search
"""

from __future__ import annotations

from typing import Dict, List, Optional


SEED_MARKET_SYMBOLS: List[Dict] = [
    # AShare
    {'market': 'AShare', 'symbol': '000001', 'name': '平安银行', 'exchange': 'SZSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 100},
    {'market': 'AShare', 'symbol': '000002', 'name': '万科A', 'exchange': 'SZSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 99},
    {'market': 'AShare', 'symbol': '600000', 'name': '浦发银行', 'exchange': 'SSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 98},
    {'market': 'AShare', 'symbol': '600036', 'name': '招商银行', 'exchange': 'SSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 97},
    {'market': 'AShare', 'symbol': '600519', 'name': '贵州茅台', 'exchange': 'SSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 96},
    {'market': 'AShare', 'symbol': '000858', 'name': '五粮液', 'exchange': 'SZSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 95},
    {'market': 'AShare', 'symbol': '002415', 'name': '海康威视', 'exchange': 'SZSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 94},
    {'market': 'AShare', 'symbol': '300059', 'name': '东方财富', 'exchange': 'SZSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 93},
    {'market': 'AShare', 'symbol': '000725', 'name': '京东方A', 'exchange': 'SZSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 92},
    {'market': 'AShare', 'symbol': '002594', 'name': '比亚迪', 'exchange': 'SZSE', 'currency': 'CNY', 'is_active': 1, 'is_hot': 1, 'sort_order': 91},

    # USStock
    {'market': 'USStock', 'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 100},
    {'market': 'USStock', 'symbol': 'MSFT', 'name': 'Microsoft Corporation', 'exchange': 'NASDAQ', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 99},
    {'market': 'USStock', 'symbol': 'GOOGL', 'name': 'Alphabet Inc.', 'exchange': 'NASDAQ', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 98},
    {'market': 'USStock', 'symbol': 'AMZN', 'name': 'Amazon.com Inc.', 'exchange': 'NASDAQ', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 97},
    {'market': 'USStock', 'symbol': 'TSLA', 'name': 'Tesla, Inc.', 'exchange': 'NASDAQ', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 96},
    {'market': 'USStock', 'symbol': 'META', 'name': 'Meta Platforms Inc.', 'exchange': 'NASDAQ', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 95},
    {'market': 'USStock', 'symbol': 'NVDA', 'name': 'NVIDIA Corporation', 'exchange': 'NASDAQ', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 94},
    {'market': 'USStock', 'symbol': 'JPM', 'name': 'JPMorgan Chase & Co.', 'exchange': 'NYSE', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 93},
    {'market': 'USStock', 'symbol': 'V', 'name': 'Visa Inc.', 'exchange': 'NYSE', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 92},
    {'market': 'USStock', 'symbol': 'JNJ', 'name': 'Johnson & Johnson', 'exchange': 'NYSE', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 91},

    # HShare
    {'market': 'HShare', 'symbol': '00700', 'name': 'Tencent Holdings', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 100},
    {'market': 'HShare', 'symbol': '09988', 'name': 'Alibaba Group', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 99},
    {'market': 'HShare', 'symbol': '03690', 'name': 'Meituan', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 98},
    {'market': 'HShare', 'symbol': '01810', 'name': 'Xiaomi Corporation', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 97},
    {'market': 'HShare', 'symbol': '02318', 'name': 'Ping An Insurance', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 96},
    {'market': 'HShare', 'symbol': '01398', 'name': 'ICBC', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 95},
    {'market': 'HShare', 'symbol': '00939', 'name': 'CCB', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 94},
    {'market': 'HShare', 'symbol': '01299', 'name': 'AIA Group', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 93},
    {'market': 'HShare', 'symbol': '02020', 'name': 'Anta Sports', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 92},
    {'market': 'HShare', 'symbol': '01024', 'name': 'Kuaishou Technology', 'exchange': 'HKEX', 'currency': 'HKD', 'is_active': 1, 'is_hot': 1, 'sort_order': 91},

    # Crypto
    {'market': 'Crypto', 'symbol': 'BTC/USDT', 'name': 'Bitcoin', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 100},
    {'market': 'Crypto', 'symbol': 'ETH/USDT', 'name': 'Ethereum', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 99},
    {'market': 'Crypto', 'symbol': 'BNB/USDT', 'name': 'BNB', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 98},
    {'market': 'Crypto', 'symbol': 'SOL/USDT', 'name': 'Solana', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 97},
    {'market': 'Crypto', 'symbol': 'XRP/USDT', 'name': 'Ripple', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 96},
    {'market': 'Crypto', 'symbol': 'ADA/USDT', 'name': 'Cardano', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 95},
    {'market': 'Crypto', 'symbol': 'DOGE/USDT', 'name': 'Dogecoin', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 94},
    {'market': 'Crypto', 'symbol': 'DOT/USDT', 'name': 'Polkadot', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 93},
    {'market': 'Crypto', 'symbol': 'MATIC/USDT', 'name': 'Polygon', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 92},
    {'market': 'Crypto', 'symbol': 'AVAX/USDT', 'name': 'Avalanche', 'exchange': 'Binance', 'currency': 'USDT', 'is_active': 1, 'is_hot': 1, 'sort_order': 91},

    # Forex (names are kept as-is from legacy dump)
    {'market': 'Forex', 'symbol': 'XAUUSD', 'name': 'Euro/US Dollar', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 100},
    {'market': 'Forex', 'symbol': 'XAGUSD', 'name': 'British Pound/US Dollar', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 99},
    {'market': 'Forex', 'symbol': 'EURUSD', 'name': 'US Dollar/Japanese Yen', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 98},
    {'market': 'Forex', 'symbol': 'GBPUSD', 'name': 'Australian Dollar/US Dollar', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 97},
    {'market': 'Forex', 'symbol': 'USDJPY', 'name': 'US Dollar/Canadian Dollar', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 96},
    {'market': 'Forex', 'symbol': 'AUDUSD', 'name': 'US Dollar/Swiss Franc', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 95},
    {'market': 'Forex', 'symbol': 'USDCAD', 'name': 'New Zealand Dollar/US Dollar', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 94},
    {'market': 'Forex', 'symbol': 'NZDUSD', 'name': 'US Dollar/Offshore Chinese Yuan', 'exchange': 'Forex', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 93},
    {'market': 'Forex', 'symbol': 'USDCHF', 'name': 'Euro/British Pound', 'exchange': 'Forex', 'currency': 'EUR', 'is_active': 1, 'is_hot': 1, 'sort_order': 92},
    {'market': 'Forex', 'symbol': 'EURJPY', 'name': 'Euro/Japanese Yen', 'exchange': 'Forex', 'currency': 'EUR', 'is_active': 1, 'is_hot': 1, 'sort_order': 91},

    # Futures
    {'market': 'Futures', 'symbol': 'CL', 'name': 'WTI Crude Oil', 'exchange': 'NYMEX', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 100},
    {'market': 'Futures', 'symbol': 'GC', 'name': 'Gold', 'exchange': 'COMEX', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 99},
    {'market': 'Futures', 'symbol': 'SI', 'name': 'Silver', 'exchange': 'COMEX', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 98},
    {'market': 'Futures', 'symbol': 'NG', 'name': 'Natural Gas', 'exchange': 'NYMEX', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 97},
    {'market': 'Futures', 'symbol': 'HG', 'name': 'Copper', 'exchange': 'COMEX', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 96},
    {'market': 'Futures', 'symbol': 'ZC', 'name': 'Corn', 'exchange': 'CBOT', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 95},
    {'market': 'Futures', 'symbol': 'ZS', 'name': 'Soybeans', 'exchange': 'CBOT', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 94},
    {'market': 'Futures', 'symbol': 'ZW', 'name': 'Wheat', 'exchange': 'CBOT', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 93},
    {'market': 'Futures', 'symbol': 'ES', 'name': 'S&P 500 E-mini', 'exchange': 'CME', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 92},
    {'market': 'Futures', 'symbol': 'NQ', 'name': 'NASDAQ 100 E-mini', 'exchange': 'CME', 'currency': 'USD', 'is_active': 1, 'is_hot': 1, 'sort_order': 91},
]


def get_hot_symbols(market: str, limit: int = 10) -> List[Dict]:
    market = (market or '').strip()
    items = [x for x in SEED_MARKET_SYMBOLS if x.get('market') == market and int(x.get('is_active', 1)) == 1 and int(x.get('is_hot', 0)) == 1]
    items.sort(key=lambda x: int(x.get('sort_order', 0)), reverse=True)
    return [{'market': x['market'], 'symbol': x['symbol'], 'name': x.get('name') or ''} for x in items[: max(limit, 0)]]


def search_symbols(market: str, keyword: str, limit: int = 20) -> List[Dict]:
    market = (market or '').strip()
    kw = (keyword or '').strip().upper()
    if not market or not kw:
        return []

    items = [x for x in SEED_MARKET_SYMBOLS if x.get('market') == market and int(x.get('is_active', 1)) == 1]
    out: List[Dict] = []

    for x in sorted(items, key=lambda i: int(i.get('sort_order', 0)), reverse=True):
        sym = str(x.get('symbol') or '').upper()
        name = str(x.get('name') or '').upper()
        if kw in sym or kw in name:
            out.append({'market': x['market'], 'symbol': x['symbol'], 'name': x.get('name') or ''})
        if len(out) >= max(limit, 0):
            break

    return out


def _normalize_for_match(market: str, symbol: str) -> str:
    m = (market or '').strip()
    s = (symbol or '').strip().upper()
    if not m or not s:
        return s

    # A-Share codes are usually 6 digits
    if m == 'AShare' and s.isdigit() and len(s) < 6:
        s = s.zfill(6)
    # H-Share codes are often 5 digits in the dump
    if m == 'HShare' and s.isdigit() and len(s) < 5:
        s = s.zfill(5)
    return s


def get_symbol_name(market: str, symbol: str) -> Optional[str]:
    """
    Best-effort exact lookup for display name.
    Returns None if not found.
    """
    m = (market or '').strip()
    if not m:
        return None

    s = _normalize_for_match(m, symbol)
    if not s:
        return None

    # Crypto: allow user to pass BTC (try BTC/USDT) or full pair.
    candidate_symbols = [s]
    if m == 'Crypto' and '/' not in s:
        candidate_symbols.append(f"{s}/USDT")

    for item in SEED_MARKET_SYMBOLS:
        if item.get('market') != m:
            continue
        item_sym = _normalize_for_match(m, str(item.get('symbol') or ''))
        for cand in candidate_symbols:
            if item_sym == cand:
                name = item.get('name')
                return str(name) if name else None

    return None


