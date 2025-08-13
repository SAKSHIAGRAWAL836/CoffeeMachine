<!DOCTYPE html>
<html lang="en">
<head>

</head>
<body>
    <h1>☕ Coffee Machine Program</h1>
    <p>
        This Python program simulates a simple coffee machine that serves
        <strong>Espresso</strong>, <strong>Latte</strong>, and <strong>Cappuccino</strong>. 
        It manages ingredient resources, processes coins, calculates change, and keeps track of profits.
    </p>

  <h2>📌 Features</h2>
    <ul>
        <li>Supports multiple drink types (<code>espresso</code>, <code>latte</code>, <code>cappuccino</code>).</li>
        <li>Checks ingredient availability before preparing a drink.</li>
        <li>Handles coin input (<code>quarters</code>, <code>dimes</code>, <code>nickels</code>, <code>pennies</code>).</li>
        <li>Calculates total money inserted and gives change.</li>
        <li>Keeps track of profits.</li>
        <li>Reports remaining resources and current profit on demand.</li>
        <li>Option to turn off the machine.</li>
    </ul>

  <h2>⚙ How It Works</h2>
    <ol>
        <li>The program starts and asks: <code>What would you like? (espresso/latte/cappuccino)</code></li>
        <li>User can type:
            <ul>
                <li><code>espresso</code>, <code>latte</code>, or <code>cappuccino</code> to order a drink</li>
                <li><code>report</code> to view resources and profit</li>
                <li><code>off</code> to turn off the machine</li>
            </ul>
        </li>
        <li>If the drink can be made with current resources, the program asks for coin input.</li>
        <li>If enough money is inserted:
            <ul>
                <li>The coffee is made</li>
                <li>Ingredients are deducted from resources</li>
                <li>Change is returned if necessary</li>
                <li>Profit is updated</li>
            </ul>
        </li>
        <li>If resources or money are insufficient, the transaction is canceled.</li>
    </ol>

  <h2>💻 Code Structure</h2>
    <ul>
        <li><code>MENU</code>: Dictionary containing drinks, ingredients, and prices.</li>
        <li><code>resources</code>: Tracks available water, milk, and coffee.</li>
        <li><code>profit</code>: Tracks earnings.</li>
        <li>
            <strong>Functions:</strong>
            <ul>
                <li><code>is_resource_sufficient(order_ingredients)</code> — Checks if enough resources are available.</li>
                <li><code>calculate_money()</code> — Calculates the total inserted coins.</li>
                <li><code>is_money_sufficient(money_paid, drink_cost)</code> — Checks payment amount and returns change if applicable.</li>
                <li><code>make_coffee(drink_name, order_ingredients)</code> — Deducts resources and serves coffee.</li>
            </ul>
        </li>
        <li>Main <code>while</code> loop handles user interaction.</li>
    </ul>

  <h2>▶ How to Run</h2>
    <ol>
        <li>Save the code in a file named <code>coffee_machine.py</code>.</li>
        <li>Run the program using:
            <pre><code>python coffee_machine.py</code></pre>
        </li>
        <li>Follow on-screen prompts to order drinks, check reports, or turn off the machine.</li>
    </ol>

  <h2>📋 Example Interaction</h2>
    
  <pre>
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.0 in change.
Here is your latte
    </pre>
  <h2>🛠 Notes</h2>
    <ul>
        <li>This is a console-based application.</li>
        <li>Ingredient and menu values can be modified in the <code>MENU</code> and <code>resources</code> dictionaries.</li>
        <li>Designed for learning purposes — not a real-world payment system.</li>
    </ul>

  <footer>
        <p><em>Made with ❤️ in Python</em></p>
    </footer>
</body>
</html>
