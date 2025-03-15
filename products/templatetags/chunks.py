from django import template

register = template.Library()

@register.filter(name = 'chunks')
def chunks(list_data, chunk_size):

    # Yield successive n-sized chunks from list_data
    # Yield is a keyword that is used like return, except the function will return a generator
    # This is a generator function that yields chunks of data
    chunk = []
    i = 0
    # Loop through the list_data
    for data in list_data:
        # Append data to chunk
        chunk.append(data)
        # Increment i
        i += 1
        # If i is equal to chunk_size
        if i == chunk_size:
            # Yield the chunk
            yield chunk
            # Reset chunk
            chunk = []
            # Reset i
            i = 0

    if chunk:
        # If i is not equal to chunk_size
        # Yield the remaining chunk
        yield chunk
   