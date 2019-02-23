import json

class Search(object):

    def __init__(self, src_paths: list = []):
        if type(src_paths) != list:
            src_paths = [src_paths]
        self.srcs = src_paths

    def _load_trans(self, path: str) -> dict:

        with open(path, 'r') as f:
            trans = json.load(f)['transactions']
            trans = filter(lambda x: x['details']['type']=='purchase', trans)
        return list(trans)

    def get_locations_by_product_type(self, product_type: str) -> list:

        locations = []
        for src in self.srcs:
            trans = self._load_trans(src)
            trans = [t for t in trans if t['metadata'].get('product_type')==product_type]
            trans = [(t['metadata']['location']['latitude'], t['metadata']['location']['longitude']) for t in trans]
            locations.extend(trans)
        return locations

    def get_customers_by_location(self, x: str, y: str, distance=0.001) -> list:
        
        x = float(x)
        y = float(y)
        # actually euclidian distance without sqrt
        def eulidian_dist(location): 
            return (float(location['latitude'])-x)**2 + (float(location['longitude'])-y)**2

        # distance = distance**2

        customers = []
        for src in self.srcs:
            trans = self._load_trans(src)
            trans = [t for t in trans if eulidian_dist(t['metadata']['location']) <= distance]
            trans = [t['this_account']['id'] for t in trans]
            
            customers.extend(trans)
        return list(set(customers))

if __name__ == '__main__':
    s = Search(['./data/test.json'])
    cs = s.get_customers_by_location('22.288077', '114.193743')
    ls = s.get_locations_by_product_type('Fashion')
    print('sth')