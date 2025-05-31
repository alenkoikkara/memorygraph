import { useState } from "react";
import SearchBar from "../components/SearchBar";
import { getSearchResults } from "../services/api-service";

interface SearchResult {
  matches: {
    url: string;
    title: string;
    summary: string;
    content: string;
    created_at: string;
  }[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

const SearchPage = () => {
  const [searchResults, setSearchResults] = useState<SearchResult>({
    matches: [],
    total: 0,
    page: 1,
    page_size: 10,
    total_pages: 1,
  });

  const handleSearch = (searchTerm: string) => {
    getSearchResults(searchTerm).then(setSearchResults);
  };

  return (
    <div className="h-screen w-full flex flex-col items-center justify-center">
      <div className="w-full max-w-md relative mb-[450px] px-4">
        <SearchBar onSearch={handleSearch} />
        <div className="mt-4 px-2 w-full flex flex-col gap-4 absolute top-10 left-0">
          {searchResults?.matches?.map((result) => (
            <div
              key={result?.created_at}
              className="cursor-pointer"
              onClick={() => {
                window.open(result?.url, "_blank");
              }}
            >
              <h2 className="text-md font-bold">{result?.title}</h2>
              <p className="text-xs text-gray-500">{result?.created_at}</p>
              <p className="text-xs text-gray-500 line-clamp-2">
                {result?.summary}
              </p>
              <p className="text-xs text-gray-500">{result?.content}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
