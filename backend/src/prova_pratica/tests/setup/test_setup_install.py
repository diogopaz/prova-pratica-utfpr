from prova_pratica import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if prova_pratica is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IProvaPraticaLayer is registered."""
        from prova_pratica.interfaces import IProvaPraticaLayer

        assert IProvaPraticaLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20240509001"
