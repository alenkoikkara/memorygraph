import { MagnifyingGlassIcon } from '@heroicons/react/24/outline'

const SearchBar = () => {
  return (
    <div className="flex items-center justify-center h-full">
      <div className="relative w-full max-w-md mx-auto">
        <div className="relative">
          <input
            type="text"
            placeholder="Search..."
            className="w-full pl-4 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <MagnifyingGlassIcon className="absolute right-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
        </div>
      </div>
    </div>
  )
}

export default SearchBar