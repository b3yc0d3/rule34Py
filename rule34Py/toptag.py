class TopTag:
    def __init__(self, rank: int, tagname: str, percentage: int):
        self._rank = rank
        self._tagname = tagname
        self._percentage = percentage
    
    def __from_dict(json: dict):
        return TopTag(json["rank"], json["tagname"], json["percentage"] * 100)
        
    @property
    def rank(self) -> int:
        """Get rank of tag

        Returns:
            int: Tag rank
        """
        return self._rank
    
    @property
    def tagname(self) -> str:
        """Get name of tag

        Returns:
            str: Tag name
        """
        return self._tagname
    
    @property
    def percentage(self) -> int:
        """Get tag usage percentage

        Returns:
            int: Usage as percentage
        """
        return self._percentage