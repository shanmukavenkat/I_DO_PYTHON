import { SignedIn, SignedOut } from "@clerk/clerk-react";
import SignInPage from "@/components/SignInPage";

import Dashboard from "@/components/Dashboard";

function App() {
  return (
   <>
   
            <SignedOut>
                <SignInPage />
            </SignedOut>
            <SignedIn>
      
                <Dashboard/>
            </SignedIn>
        
   </>
  );
}

export default App;