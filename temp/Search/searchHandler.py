from . import catSearch
from . import dogSearch

def search():
    dogSearch.search()
    catSearch.search()

if __name__ == "__main__":
    search()