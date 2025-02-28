import pytest


def test_our_first_test() -> None:
    assert 1 == 1


# use this to skip a test
@pytest.mark.skip
# this will skip the test
def test_should_be_skipped() -> None:
    assert 1 == 2


@pytest.mark.skipif(4 > 1, reason="Skipped because 4>1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2


@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 1


@pytest.mark.slow
def test_with_custom_mark1() -> None:
    pass


# pytest ./gist/test_gist.py -v -p no:warnings
# this will show no warnings with the " -p no:warnings"

# pytest ./gist/test_gist.py -v -p no:warnings -m slow
# this will only run the test that are marked as "slow"
# -m = marked as

# pytest ./gist/test_gist.py -v -p no:warnings -m "not slow"
# this will run everything that is not marked as slow


class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"


@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR")


def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")


# pytest ./gist/test_gist.py -v -s
#  -s flag will show any print statements


@pytest.mark.parametrize(
    "company_name",
    ["Tiktok", "Instagram", "Twitch"],
    ids=["TIKTOK TEST", "INSTAGRAM TEST", "TWITCH TEST"],
)
def test_parametrized(company_name: str) -> None:
    print(f"\nTest with {company_name}")


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


def test_raise_covid_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)
