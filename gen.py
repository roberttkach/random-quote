This Python script generates a random quote by fetching data from the [Quotable API](https://github.com/lukePeavey/quotable). It uses the `requests` library to make an HTTP GET request to the API endpoint and the `json` library to parse the JSON response.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- `requests`: You can install it using `pip install requests`.

## Usage

1. Save the script to a Python file (e.g., `quote_generator.py`).
2. Open your terminal or command prompt, navigate to the directory where the script is saved.
3. Run the script using the following command:

```bash
python quote_generator.py
```

The script will print a random quote along with its author in the format `"Quote" - Author`.

## How it Works

The script defines a function called `get_quote()` that performs the following steps:

1. It uses the `requests.get()` function to send an HTTP GET request to the `https://api.quotable.io/random` endpoint, which retrieves a random quote from the Quotable API.
2. The API response is stored in the `response` variable.
3. The `json.loads(response.text)` function is used to parse the JSON response data from the API into a Python dictionary, which is stored in the `json_data` variable.
4. The quote text and author are extracted from the `json_data` dictionary using the keys `'content'` and `'author'`, respectively.
5. The function returns a formatted string containing the quote and author, using an f-string.

In the main part of the script, the `get_quote()` function is called, and its output is printed to the console using the `print()` function.

## API Endpoint

The script uses the following API endpoint to fetch random quotes:

- `https://api.quotable.io/random`

This endpoint returns a JSON response with the following structure:

```json
{
  "_id": "quote_id",
  "content": "Quote text",
  "author": "Author name",
  "tags": ["tag1", "tag2", ...],
  "authorSlug": "author_slug",
  "length": 100,
  "dateAdded": "2023-05-23",
  "dateModified": "2023-05-23"
}
```

For more information about the Quotable API, please refer to the [official documentation](https://github.com/lukePeavey/quotable).

## Dependencies

- `requests`: A Python library for making HTTP requests. You can install it using `pip install requests`.
- `json`: A built-in Python library for working with JSON data.

Note: This script assumes that you have a working internet connection, as it fetches data from an external API.
