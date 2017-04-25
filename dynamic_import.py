import_name = 'numpy'
import_module = __import__(import_name)

np = import_module

print(np.__version__)

a = np.arange(15).reshape(3, 5)
print(a)