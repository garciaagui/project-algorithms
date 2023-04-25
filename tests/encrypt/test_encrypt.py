from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    even_expected = "noht_yP"
    odd_expected = "tyP_noh"
    reversed_expected = "nohtyP"

    # Even key
    even_result = encrypt_message("Python", 2)
    assert even_expected == even_result

    # Odd key
    odd_result = encrypt_message("Python", 3)
    assert odd_expected == odd_result

    # Out of range key
    reversed_result = encrypt_message("Python", 10)
    assert reversed_expected == reversed_result

    # Invalid message
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 2)

    # Invalid key
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Python", "invalid")
