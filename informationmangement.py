# Rule-based Expert System for Information Management

def get_info_recommendation(file_size, file_type):
    if file_size < 10 and file_type == 'Text':
        return 'Store in local folder'
    elif file_size >= 10 and file_size < 100 and file_type == 'Image':
        return 'Store in cloud storage'
    elif file_size >= 100 and file_type == 'Video':
        return 'Archive in external hard drive'
    else:
        return 'No recommendation'

# Example usage
file_size = 50
file_type = 'Image'

recommendation = get_info_recommendation(file_size, file_type)
print('Information Recommendation:', recommendation)
