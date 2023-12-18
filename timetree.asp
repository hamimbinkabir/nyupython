<%
Dim i1, i2, lt, rt, dt
Dim lt_suffix, rt_suffix, dt_suffix

' Check if the form is submitted
If Request.ServerVariables("REQUEST_METHOD") = "POST" Then
    ' Get the input values from the form
    i1 = Request.Form("time")
    i2 = Request.Form("city")
    
    ' Validate the input values
    If Len(i1) <> 4 Or Not IsNumeric(i1) Then
        Response.Write("Invalid input! Please enter the time in HHMM format.")
        Response.End
    End If
    
    If i2 <> "1" And i2 <> "2" And i2 <> "3" Then
        Response.Write("Invalid input! Please enter a valid option.")
        Response.End
    End If
    
    ' Convert the input to integer
    i1 = CInt(i1)
    
    ' Calculate the time for each city
    If i2 = "1" Then
        lt = i1 - 600
        rt = i1 - 300
        dt = i1
    ElseIf i2 = "2" Then
        lt = i1 - 300
        rt = i1 
        dt = i1 + 300
    ElseIf i2 = "3" Then
        lt = i1
        rt = i1 + 300
        dt = i1 + 600
    End If
    
    ' Handling cases where the time is greater than 2400 or less than 0
    If dt > 2400 Then
        dt = dt - 2400
        dt_suffix = " following"
    ElseIf dt < 0 Then
        dt = dt + 2400
        dt_suffix = " previous"
    Else
        dt_suffix = " current"
    End If
    
    If rt > 2400 Then
        rt = rt - 2400
        rt_suffix = " following"
    ElseIf rt < 0 Then
        rt = rt + 2400
        rt_suffix = " previous"
    Else
        rt_suffix = " current"
    End If
    
    If lt > 2400 Then
        lt = lt - 2400
        lt_suffix = " following"
    ElseIf lt < 0 Then
        lt = lt + 2400
        lt_suffix = " previous"
    Else
        lt_suffix = " current"
    End If
End If
%>

<!DOCTYPE html>
<html>
<head>
    <title>Time Converter</title>
</head>
<body>
    <h1>Time Converter</h1>
    
    <form method="post" action="treetime.asp">
        <label for="time">Time[HHMM]:</label>
        <input type="text" id="time" name="time" maxlength="4" required pattern="\d{4}">
        
        <br>
        
        <label for="city">City:</label>
        <select id="city" name="city" required>
            <option value="1">Dhaka</option>
            <option value="2">Riyadh</option>
            <option value="3">London</option>
        </select>
        
        <br>
        
        <input type="submit" value="Convert">
    </form>
    
    <br>
    
    <% If Request.ServerVariables("REQUEST_METHOD") = "POST" Then %>
    <h2>Results:</h2>
    <p>
        Dhaka time: <%= dt %> <%= dt_suffix %> <br>
        Riyadh time: <%= rt %> <%= rt_suffix %> <br>
        London time: <%= lt %> <%= lt_suffix %>
    </p>
    <% End If %>
</body>
</html>
