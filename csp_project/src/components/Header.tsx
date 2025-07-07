import { UserButton } from "@clerk/clerk-react";
import { useUser } from "@clerk/clerk-react";

const Header = () => {
    const { user } = useUser();
    
    return (
        <header className="bg-blue-400 text-black p-4 flex justify-between items-center shadow-md">
    <div className="flex items-center gap-4">
        <UserButton
            appearance={{
                elements: {
                    userButtonAvatarBox: "size-10"
                }
            }}
        />
        {user && <h1 className="text-lg font-medium">{user.firstName} {user.lastName}</h1>}
    </div>
</header>

    );
};

export default Header;
