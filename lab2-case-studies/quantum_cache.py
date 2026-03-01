from quantum_cache import QuantumCache

#initialize a distributed quantum cache with a maximum size of 100 items
cache = QuantumCache(max_size=100) 

#A example of using the cache to store and retrieve data
cache.set("key1", "value1")
print(cache.get("key1"))  # Output: value1
cache.set("key2", "value2")
print(cache.get("key2"))  # Output: value2
cache.delete("key1")
print(cache.get("key1"))  # Output: None (since key1 has been deleted)
