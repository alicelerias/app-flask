import { QueryClientProvider, QueryClient } from "react-query";

import { Form } from "./components/Form";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
    },
  },
});

function App() {
  return (
    <div className="bg-gray-200">
      <QueryClientProvider client={queryClient}>
        <Form />
      </QueryClientProvider>
    </div>
  );
}

export default App;
