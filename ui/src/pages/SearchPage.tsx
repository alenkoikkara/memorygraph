import { useState } from "react";
import SearchBar from "../components/SearchBar";
import { getSearchResults } from "../services/api-service";

interface SearchResult {
  url: string;
  title: string;
  summary: string;
  content: string;
  created_at: string;
}

const SearchPage = () => {
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);

  const handleSearch = (searchTerm: string) => {
    getSearchResults(searchTerm).then(setSearchResults);
  };

  return (
    <div className="h-screen w-full flex flex-col items-center justify-center">
      <div className="w-full max-w-md relative">
        <SearchBar onSearch={handleSearch} />
        <div className="mt-4 px-2 w-full flex flex-col gap-4 absolute top-10 left-0">
          {searchResults.map((result: SearchResult) => (
            <div
              key={result.created_at}
              className="cursor-pointer"
              onClick={() => {
                window.open(result.url, "_blank");
              }}
            >
              <h2 className="text-md font-bold">{result.title}</h2>
              <p className="text-xs text-gray-500">{result.created_at}</p>
              <p className="text-xs text-gray-500 line-clamp-2">{result.summary}</p>
              <p className="text-xs text-gray-500">{result.content}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
