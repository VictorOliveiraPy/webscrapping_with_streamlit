from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi import Query

from repository.database import TransactionsTable

item_router = APIRouter()

repository = TransactionsTable()


@item_router.get("", status_code=200)
def get_items(page_size: Optional[int] = Query(10, gt=0)):
    response = repository.get_items(page_size)
    print(response)
    if not response:
        raise HTTPException(status_code=404, detail="Items not found")
    return repository.get_items(page_size)
