from pathlib import Path
from pycrypto import __version__

import hmac
import hashlib


def test_version():
    assert __version__ == "0.1.0"


def test_hash_signature():
    # with open(Path.home() / Path("Downloads/Python-3.10.4.tar.xz"), "br") as f:
    #    content = f.read()
    # signature = hashlib.md5(content).hexdigest()
    # assert signature == "21f2e113e087083a1e8cf10553d93599"

    # echo -n "test" | md5sum -> 098f6bcd4621d373cade4e832627b4f6
    known_signature = "098f6bcd4621d373cade4e832627b4f6"
    signature = hashlib.md5("test".encode("utf-8")).hexdigest()
    assert signature == known_signature


def test_hmac_sha256():
    key = "key"
    message = "The quick brown fox jumps over the lazy dog"
    hmac_sha256 = hmac.new(bytes(key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
    assert (
        hmac_sha256.hexdigest()
        == "f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8"
    )
