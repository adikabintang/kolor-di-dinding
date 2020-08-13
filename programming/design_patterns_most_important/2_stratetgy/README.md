# Strategy pattern

Strategy pattern allows selecting algorithm at runtime.

The idea is:

- Have a `Strategy` interface
- The implementation is done by class that inherits that `Strategy`

Example:

```cpp
// Strategy
class Sort {
    public:
        virtual void sort(std::vector<int> &v);
};

class BubbleSort : public Sort {
    public:
        void sort(std::vector<int> &v) override {
            // implement bubble sort
        }
};

class MergeSort : public Sort {
    public:
        void sort(std::vector<int> &v) override {
            // implement merge sort
        }
}

class SortingProgram {
    private:
        std::vector<int> v;
    public:
        SortingProgram(std::vector<int> v) {
            this->v = v;
        }

        void runSort(Sort alg) {
            alg.sort(this->v);
        }
}
// we can use it like this:
std::vector<int> v{4, 2, 6, 1, 1, 2};
auto sp = SortingProgram(v);
sp.runSort(MergeSort());
```

### Auth program example

For example, if we have several auth methods to impement, we can do it like this:

```python
class BasicAuth:
    pass

class OAuth:
    pass

class OpenIDAuth:
    pass

class AuthProgram:
    def authenticate(self, method):
        if method == "basic":
            # use BasicAuth
        elif method == "oauth":
            # use OAuth
        elif method == "openid":
            # use OpenIDAuth
```

If we add a new method, we need to add to the `if` chain.

Look at the [python auth example](0_python_auth.py) to see the implementatiton using strategy pattern.

Credit:

- https://blog.bitsrc.io/keep-it-simple-with-the-strategy-design-pattern-c36a14c985e9
