from hindsight_client import Hindsight

from backend.config.settings import (
    HINDSIGHT_BASE_URL,
    HINDSIGHT_API_KEY,
    HINDSIGHT_BANK_ID,
)


client = Hindsight(
    base_url=HINDSIGHT_BASE_URL,
    api_key=HINDSIGHT_API_KEY,
)


async def initialize_memory_async():
    """
    Create the Hindsight organizational memory bank.
    """

    try:
        await client.acreate_bank(
            bank_id=HINDSIGHT_BANK_ID,
            name="MemoryOps Organizational Memory",
        )

        print(f"Created Hindsight bank: {HINDSIGHT_BANK_ID}")

    except Exception as exc:
        print(f"Hindsight bank initialization: {exc}")


def initialize_memory():
    """
    Synchronous initialization for scripts/tests.
    """

    try:
        client.create_bank(
            bank_id=HINDSIGHT_BANK_ID,
            name="MemoryOps Organizational Memory",
        )

        print(f"Created Hindsight bank: {HINDSIGHT_BANK_ID}")

    except Exception as exc:
        print(f"Hindsight bank initialization: {exc}")


def retain_memory(content: str, context: str = "incident response"):
    return client.retain(
        bank_id=HINDSIGHT_BANK_ID,
        content=content,
        context=context,
    )


def recall_memory(query: str):
    return client.recall(
        bank_id=HINDSIGHT_BANK_ID,
        query=query,
    )


def close_memory():
    client.close()