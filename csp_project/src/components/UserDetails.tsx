import { useSession, useUser } from "@clerk/clerk-react";

const UserDetails = () => {
    const { user } = useUser();
    const { session } = useSession();

    if (!user || !session) return null;

    const formatDate = (date: string | number | Date | null) => {
        return date ? new Date(date).toLocaleDateString("en-US", {
            month: "short",
            day: "numeric",
            year: "numeric",
        }) : "N/A";
    };

    return (
        <>
            
          <div className="min-h-screen bg-white text-white p-8 flex justify-center items-center">
            <div className="grid grid-cols-4 gap-6 w-full max-w-6xl">
                {/* Full-Width Profile Image */}
                <div className="col-span-4 lg:col-span-2 h-64 rounded-2xl overflow-hidden">
                    <img className="w-full h-full object-cover" src={user.imageUrl} alt="User Profile" />
                </div>

                {/* User Info (Name, Email) */}
                <div className="col-span-4 lg:col-span-2 bg-blue-900 p-6 rounded-2xl shadow-lg flex flex-col justify-center">
                <h1 className="text-2xl font-semibold">Welcome 👋</h1>
                <h1 className="text-lg mt-2">Hello, great to see you here!</h1>
                    <h1 className="text-2xl font-semibold">{user.firstName} {user.lastName}</h1>
                    <p className="text-gray-400 text-sm mt-2">📧{user.emailAddresses[0].emailAddress}</p>
                </div>

                {/* Last Sign-in */}
                <div className="col-span-2 bg-gray-800 p-6 rounded-2xl shadow-md">
                    <span className="text-gray-400 font-semibold">Last Sign-in:</span>
                    <p className="text-white text-sm">{formatDate(user.lastSignInAt)}</p>
                </div>

                {/* Created At */}
                <div className="col-span-2 bg-gray-800 p-6 rounded-2xl shadow-md">
                    <span className="text-gray-400 font-semibold">Created At:</span>
                    <p className="text-white text-sm">{formatDate(user.createdAt)}</p>
                </div>

                {/* User ID */}
                <div className="col-span-4 bg-gray-800 p-6 rounded-2xl shadow-md text-center">
                    <span className="text-gray-400 font-semibold">User ID:</span>
                    <p className="text-white text-sm break-all">{user.id}</p>
                </div>
            </div>
        </div>
        </>
    );
};

export default UserDetails;
