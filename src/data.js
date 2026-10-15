export const starterProducts=[
{id:1,name:"Coca-Cola 500ml",category:"Drinks",qty:24,cost:1200,price:2000},
{id:2,name:"Bottled Water",category:"Drinks",qty:32,cost:500,price:1000},
{id:3,name:"Wheat Flour 1kg",category:"Food",qty:8,cost:1800,price:2500},
{id:4,name:"Laundry Soap",category:"Household",qty:4,cost:1500,price:2200}];
export const starterSales=[{id:101,product:"Coca-Cola 500ml",qty:5,total:10000,date:new Date().toISOString(),cost:6000},{id:102,product:"Wheat Flour 1kg",qty:2,total:5000,date:new Date().toISOString(),cost:3600}];
export const starterExpenses=[{id:201,title:"Transport",category:"Transport",amount:8000,date:new Date().toISOString()},{id:202,title:"Shop supplies",category:"Supplies",amount:12000,date:new Date().toISOString()}];
export const starterDebts=[{id:301,customer:"Juma Ally",phone:"",amount:15000,note:"Outstanding"}];
export function readStore(key,fallback){try{const value=localStorage.getItem(key);return value===null?fallback:JSON.parse(value)}catch{return fallback}}
export const money=value=>new Intl.NumberFormat("en-TZ",{style:"currency",currency:"TZS",maximumFractionDigits:0}).format(Number(value)||0);
