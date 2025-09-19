import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { cn } from "@/lib/utils";
import {
  LayoutDashboard,
  Receipt,
  PiggyBank,
  TrendingUp,
  Share2,
  Settings,
  Menu,
  Plus,
} from "lucide-react";

const navigationItems = [
  { icon: LayoutDashboard, label: "Dashboard", path: "/", active: true },
  { icon: Receipt, label: "Transactions", path: "/transactions" },
  { icon: PiggyBank, label: "Budgets", path: "/budgets" },
  { icon: TrendingUp, label: "Analytics", path: "/analytics" },
  { icon: Share2, label: "Sharing", path: "/sharing" },
  { icon: Settings, label: "Settings", path: "/settings" },
];

export function MobileNav() {
  const [open, setOpen] = useState(false);

  return (
    <>
      {/* Mobile Header */}
      <div className="flex h-16 items-center justify-between px-4 border-b bg-card lg:hidden">
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 bg-gradient-primary rounded-lg flex items-center justify-center">
            <PiggyBank className="w-5 h-5 text-primary-foreground" />
          </div>
          <h1 className="text-xl font-bold bg-gradient-primary bg-clip-text text-transparent">
            FinanceApp
          </h1>
        </div>
        
        <div className="flex items-center space-x-2">
          <Button size="sm" className="bg-gradient-primary shadow-card">
            <Plus className="w-4 h-4" />
          </Button>
          <Sheet open={open} onOpenChange={setOpen}>
            <SheetTrigger asChild>
              <Button variant="ghost" size="sm">
                <Menu className="w-5 h-5" />
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-64 p-0">
              <div className="flex h-full flex-col">
                {/* Header */}
                <div className="flex h-16 items-center px-4 border-b">
                  <div className="flex items-center space-x-2">
                    <div className="w-8 h-8 bg-gradient-primary rounded-lg flex items-center justify-center">
                      <PiggyBank className="w-5 h-5 text-primary-foreground" />
                    </div>
                    <h1 className="text-xl font-bold bg-gradient-primary bg-clip-text text-transparent">
                      FinanceApp
                    </h1>
                  </div>
                </div>

                {/* Navigation */}
                <nav className="flex-1 p-4 space-y-2">
                  {navigationItems.map((item) => {
                    const Icon = item.icon;
                    return (
                      <Button
                        key={item.path}
                        variant={item.active ? "default" : "ghost"}
                        className={cn(
                          "w-full justify-start h-12 transition-all duration-200",
                          item.active && "bg-gradient-primary text-primary-foreground shadow-card"
                        )}
                        onClick={() => setOpen(false)}
                      >
                        <Icon className="w-5 h-5 mr-3" />
                        <span className="font-medium">{item.label}</span>
                      </Button>
                    );
                  })}
                </nav>

                {/* User Profile */}
                <div className="p-4 border-t">
                  <div className="flex items-center space-x-3 p-3 rounded-lg bg-muted">
                    <div className="w-8 h-8 bg-gradient-primary rounded-full flex items-center justify-center">
                      <span className="text-sm font-medium text-primary-foreground">JD</span>
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium truncate">John Doe</p>
                      <p className="text-xs text-muted-foreground truncate">john@example.com</p>
                    </div>
                  </div>
                </div>
              </div>
            </SheetContent>
          </Sheet>
        </div>
      </div>

      {/* Mobile Bottom Navigation */}
      <div className="fixed bottom-0 left-0 right-0 bg-card border-t lg:hidden z-50">
        <div className="grid grid-cols-5 gap-1 p-2">
          {navigationItems.slice(0, 5).map((item) => {
            const Icon = item.icon;
            return (
              <Button
                key={item.path}
                variant="ghost"
                size="sm"
                className={cn(
                  "flex flex-col h-12 p-2 space-y-1",
                  item.active && "text-primary"
                )}
              >
                <Icon className="w-4 h-4" />
                <span className="text-xs font-medium">{item.label}</span>
              </Button>
            );
          })}
        </div>
      </div>
    </>
  );
}