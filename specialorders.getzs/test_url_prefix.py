#!/usr/bin/env python3
"""
Test script to verify URL prefix configuration
"""
import os
from app import create_app

def test_url_prefix():
    """Test the URL prefix configuration"""
    
    # Test without URL prefix (development)
    print("Testing without URL prefix...")
    app_dev = create_app('development')
    print(f"Development URL_PREFIX: {app_dev.config.get('URL_PREFIX', 'None')}")
    
    # Test with URL prefix (production)
    print("\nTesting with URL prefix...")
    app_prod = create_app('production')
    print(f"Production URL_PREFIX: {app_prod.config.get('URL_PREFIX', 'None')}")
    
    # Test with custom URL prefix
    print("\nTesting with custom URL prefix...")
    os.environ['URL_PREFIX'] = '/testApp'
    app_custom = create_app('production')
    print(f"Custom URL_PREFIX: {app_custom.config.get('URL_PREFIX', 'None')}")
    
    print("\nURL prefix configuration test completed!")

if __name__ == "__main__":
    test_url_prefix() 