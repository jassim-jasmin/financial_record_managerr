import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import {
  Wallet,
  TrendingUp,
  TrendingDown,
  PiggyBank,
  ArrowUpRight,
  ArrowDownRight,
  Plus,
} from "lucide-react";

interface StatsCardProps {
  title: string;
  value: string;
  change: string;
  changeType: "positive" | "negative";
  icon: React.ReactNode;
}

function StatsCard({ title, value, change, changeType, icon }: StatsCardProps) {
  return (
    <Card className="bg-gradient-card shadow-card hover:shadow-elevated transition-all duration-200">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">
          {title}
        </CardTitle>
        <div className="w-8 h-8 bg-primary/10 rounded-lg flex items-center justify-center">
          {icon}
        </div>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold text-card-foreground">{value}</div>
        <div className="flex items-center text-xs mt-1">
          {changeType === "positive" ? (
            <ArrowUpRight className="w-3 h-3 text-success mr-1" />
          ) : (
            <ArrowDownRight className="w-3 h-3 text-destructive mr-1" />
          )}
          <span className={changeType === "positive" ? "text-success" : "text-destructive"}>
            {change}
          </span>
          <span className="text-muted-foreground ml-1">from last month</span>
        </div>
      </CardContent>
    </Card>
  );
}

interface BudgetCardProps {
  category: string;
  spent: number;
  budget: number;
  color: string;
}

function BudgetCard({ category, spent, budget, color }: BudgetCardProps) {
  const percentage = (spent / budget) * 100;
  const remaining = budget - spent;
  
  return (
    <Card className="bg-gradient-card shadow-card">
      <CardContent className="p-4">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm font-medium">{category}</span>
          <span className="text-xs text-muted-foreground">
            ${remaining.toFixed(0)} left
          </span>
        </div>
        <div className="space-y-2">
          <div className="flex items-center justify-between text-sm">
            <span className="text-muted-foreground">${spent.toFixed(0)}</span>
            <span className="text-muted-foreground">${budget.toFixed(0)}</span>
          </div>
          <Progress 
            value={percentage} 
            className="h-2"
            style={{ 
              "--progress-background": color,
            } as React.CSSProperties}
          />
        </div>
      </CardContent>
    </Card>
  );
}

export function DashboardCards() {
  const stats = [
    {
      title: "Total Balance",
      value: "$12,345.67",
      change: "+12.5%",
      changeType: "positive" as const,
      icon: <Wallet className="w-4 h-4 text-primary" />,
    },
    {
      title: "Monthly Income",
      value: "$5,250.00",
      change: "+4.2%",
      changeType: "positive" as const,
      icon: <TrendingUp className="w-4 h-4 text-success" />,
    },
    {
      title: "Monthly Expenses",
      value: "$3,127.48",
      change: "-8.1%",
      changeType: "positive" as const,
      icon: <TrendingDown className="w-4 h-4 text-destructive" />,
    },
    {
      title: "Savings Rate",
      value: "40.4%",
      change: "+2.3%",
      changeType: "positive" as const,
      icon: <PiggyBank className="w-4 h-4 text-success" />,
    },
  ];

  const budgets = [
    { category: "Food & Dining", spent: 450, budget: 600, color: "hsl(var(--primary))" },
    { category: "Transportation", spent: 280, budget: 400, color: "hsl(var(--success))" },
    { category: "Shopping", spent: 320, budget: 500, color: "hsl(var(--warning))" },
    { category: "Entertainment", spent: 180, budget: 200, color: "hsl(var(--destructive))" },
  ];

  return (
    <div className="space-y-6">
      {/* Stats Overview */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat, index) => (
          <StatsCard key={index} {...stat} />
        ))}
      </div>

      {/* Quick Actions */}
      <Card className="bg-gradient-card shadow-card">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            Quick Actions
            <Button size="sm" className="bg-gradient-primary shadow-card">
              <Plus className="w-4 h-4 mr-2" />
              Add Transaction
            </Button>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid gap-3 md:grid-cols-3">
            <Button variant="outline" className="h-12 justify-start">
              <TrendingUp className="w-4 h-4 mr-2 text-success" />
              Add Income
            </Button>
            <Button variant="outline" className="h-12 justify-start">
              <TrendingDown className="w-4 h-4 mr-2 text-destructive" />
              Add Expense
            </Button>
            <Button variant="outline" className="h-12 justify-start">
              <PiggyBank className="w-4 h-4 mr-2 text-primary" />
              Set Budget
            </Button>
          </div>
        </CardContent>
      </Card>

      {/* Budget Overview */}
      <div className="grid gap-4 md:grid-cols-2">
        <Card className="bg-gradient-card shadow-card">
          <CardHeader>
            <CardTitle>Budget Overview</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            {budgets.map((budget, index) => (
              <BudgetCard key={index} {...budget} />
            ))}
          </CardContent>
        </Card>

        <Card className="bg-gradient-card shadow-card">
          <CardHeader>
            <CardTitle>Recent Transactions</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {[
                { name: "Grocery Store", amount: -85.32, category: "Food", date: "Today" },
                { name: "Salary Deposit", amount: 2625.00, category: "Income", date: "Yesterday" },
                { name: "Gas Station", amount: -45.20, category: "Transportation", date: "2 days ago" },
                { name: "Netflix", amount: -15.99, category: "Entertainment", date: "3 days ago" },
              ].map((transaction, index) => (
                <div key={index} className="flex items-center justify-between p-3 rounded-lg bg-muted/50">
                  <div className="flex-1">
                    <p className="font-medium text-sm">{transaction.name}</p>
                    <p className="text-xs text-muted-foreground">
                      {transaction.category} • {transaction.date}
                    </p>
                  </div>
                  <span className={`font-medium text-sm ${
                    transaction.amount > 0 ? "text-success" : "text-destructive"
                  }`}>
                    {transaction.amount > 0 ? "+" : ""}${Math.abs(transaction.amount).toFixed(2)}
                  </span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}