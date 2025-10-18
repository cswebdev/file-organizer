import os

FILE_TYPE_MAPPINGS = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp', '.tiff'],
    'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.odt'],
    'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'video': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'installers': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
    'code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.rb', '.php', '.go', '.rs'],
}

DEFAULT_DESTINATION_FOLDERS = {
    'images': 'SortedFiles/images',
    'documents': 'SortedFiles/documents',
    'audio': 'SortedFiles/audio',
    'video': 'SortedFiles/video',
    'archives': 'SortedFiles/archives',
    'installers': 'SortedFiles/installers',
    'code': 'SortedFiles/code',
    'others': 'SortedFiles/others',
}

def get_extension_mapping(base_path=None, include_unknown=True):
    """Creates a mapping from file extensions to their destination folders."""
    if base_path is None:
        base_path = os.expanduser("~/SortedFiles")

    extension_mapping = {}
    for category, extensions in FILE_TYPE_MAPPINGS.items():
        destination = os.path.join(base_path, category.title())
        for ext in extensions:
            extension_mapping[ext] = destination
        
    if include_unknown:
        extension_mapping['.unknown'] = os.path.join(base_path, "Others")
        
    return extension_mapping

