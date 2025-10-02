print ('Welcome to this Nokia menu map ')
print('1 - Phone book')
print('2 - Messages')
print('3 - Chat')
print('4 - Call register')
print('5 - Tones')
print('6 - Settings')
print('7 - Call divert')
print('8 - Games')
print('9 - Calculator')
print('10 - Reminders')
print('11 - Clock')
print('12 - Profiles')
print('13 - SIM services')	
match choice:
	case 1:
		print("====Phone book====")
		print("1. Search")
		print("2. Service Nos")
		print("3. Add name")
		print("4. Erase")
		print("5. Edit")
		print("6. Assign Tone")
		print("7. Send b' card")
		print("8. Options")
		print("9. Speed dials")
		print("10. Voice tags")
		match first_choice :
				
					case 1:
						under_first_choice = 0
						while under_first_choice != 2:
							print("1. Search")
							print("2. Back")
							under_first_choice = int(input("Enter 2 to quit: "))
							if under_first_choice == 2:
								break
							
					case 2:
						under_second_choice = 0
						while under_second_choice != 3:
							print("2. Service Nos")
							print("3. Back")
							under_second_choice = int(input("Enter 3 to quit: "))
							if under_second_choice ==3:
								break
					case 3:
						under_third_choice = 0
						while under_third_choice != 4:
							print("3. Add name")
							print("4. Back")
							under_third_choice = int(input("Enter 4 to quit: "))
							if under_third_choice == 4:
								break
					case 4:
						under_fourth_choice = 0
						while under_fourth_choice != 5:
							print("4. Erase")
							print("5. Back")
							under_fourth_choice = int(input("Enter 5 to quit: "))
							if under_fourth_choice == 5:
								break
					case 5:
						under_fifth_choice = 0
						while under_fifth_choice != 6:
							print("5. Edit")
							print("6. Back")
							under_fifth_choice = int(input("Enter 6 to quit: "))
							if under_fifth_choice == 6:
								break
					case 6:
						under_sixth_choice = 0
						while under_sixth_choice != 7:
							print("6. Assign Tone")
							print("7. Back")
							under_sixth_choice = int(input("Enter 7 to quit: "))
							if under_sixth_choice == 7:
								break
					case 7:
						under_seventh_choice = 0
						while under_seventh_choice != 8:
							print("7. Send b' card")
							print("8. Back")
							under_seventh_choice = int(input("Enter 8 to quit: "))
							if under_seventh_choice == 8:
								break
					case 8:
						under_eightth_choice = 0
						while under_eightth_choice != 9:
							print("8. Options")
							print("1. Type of view")
							print("2. Memory status")
							print("9. Back")
							under_eightth_choice = int(input("Enter your choice: "))
							if under_eightth_choice == 9:
								break
							match under_eightth_choice:
								case 1:
									under_eight1 = 0
									while under_eight1 != 2:
										print("1. Type of view")
										under_eight1 = int(input("Enter 2 to quit: "))
										if under_eight1 == 2:
											break
								case 2:
									under_eight2 = 0
									while under_eight2 != 3:
										print("2. Memory status")
										under_eight2 = int(input("Enter 3 to quit: "))
										if under_eight2 == 3:
											break
					case 9:
						under_nineth_choice = 0
						while under_nineth_choice != 10:
							print("9. Speed dials")
							print("10. Back")
							under_nineth_choice = int(input("Enter 10 to quit: "))
							if under_nineth_choice == 10:
								break
					case 10:
						under_tenth_choice = 0
						while under_tenth_choice != 11:
							print("10. Voice tags")
							print("11. Back")
							under_tenth_choice = int(input("Enter 11 to quit: "))
							if under_tenth_choice == 11:
								break
						break

		case 2:
			second_choice = 0
			while second_choice != 11:
				print("====Messages====")
				print("1. Write messages")
				print("2. Inbox")
				print("3. Outbox")
				print("4. Picture messages")
				print("5. Templates")
				print("6. Smileys")
				print("7. Messages settngs")
				print("8. Info service")
				print("9. Voice mailbox number")
				print("10. Service command editor")
				print("11. Back")
				second_choice = int(input("Enter your choice: "))
				match second_choice:
					case 1:
						under_one = 0
						while under_one !=2:
							print("1. Write messages")
							print("2 Back: ")
							under_one = int(input("Enter 2 to quit: "))
							if under_one == 2:
								break
					case 2:
						under_two = 0
						while under_two !=3:
							print("2. Inbox")
							print("3 Back: ")
							under_two = int(input("Enter 3 to quit: "))
							if under_two == 3:
								break
					case 3:
						under_three = 0
						while under_three !=4:
							print("3. Outbox")
							print("4 Back: ")
							under_three = int(input("Enter 4 to quit: "))
							if under_three == 4:
								break
					case 4:
						under_four = 0
						while under_four !=5:
							print("4. Picture messages")
							print("5 Back: ")
							under_four = int(input("Enter 5 to quit: "))
							if under_four == 5:
								break
					case 5:
						under_five = 0
						while under_five !=6:
							print("5. Templates")
							print("6 Back: ")
							under_five = int(input("Enter 6 to quit: "))
							if under_five == 6:
								break
					case 6:
						under_six = 0
						while under_six !=7:
							print("6. Smileys")
							print("7 Back: ")
							under_six = int(input("Enter 7 to quit: "))
							if under_six == 7:
								break
					case 7:
						under_seven = 0
						while under_seven !=8:
							print("7. Messages settngs")
							#print("8 Back: ")
							print("1. Set 1")
							print("2. Common")
							match under_seven:
								case 1:
									under_seven1 = 0
									while under_seven1 != 4:
										print("Set 1")
										print("1. Message centre number")
										print("2. Message sent as")
										print("3. Message validity")
										print("4. Back")
										under_seven1 = int(input("Enter your choice: "))
										if under_seven1 == 4:
											break
									
								case 2:
									under_seven2 = 0
									while under_seven2 != 4:
										print("Common")
										print("1. Delivery reports")
										print("2. Reply via same centre")
										print("3. Character support")
										print("4. Back")
										under_seven2 = int(input("Enter your choice: "))
										if under_seven2 == 4:
											break
							under_seven = int(input("Enter 8 to quit: "))
							if under_seven == 8:
								break
					case 8:
						under_eight = 0
						while under_eight !=9:
							print("8. Info service")
							print("9 Back: ")
							under_eight = int(input("Enter 9 to quit: "))
							if under_eight == 9:
								break
					case 9:
						under_nine = 0
						while under_nine !=10:
							print("9. Voice mailbox number")
							print("10 Back: ")
							under_nine = int(input("Enter 10 to quit: "))
							if under_nine == 10:
								break
					case 10:
						under_ten = 0
						while under_ten !=11:
							print("10. Service command editor")
							print("11. Back: ")
							under_ten = int(input("Enter 11 to quit: "))
							if under_ten == 11:
								break
						break
		case 3:
			print("Chat")
		case 4:
			fourth_choice = 0
			while fourth_choice != 9:
				print("====Call register====")
				print("1. Missed calls")
				print("2. Received calls")
				print("3. Dialled numbers")
				print("4. Erase recent call lists")
				print("5. Show call duration")
				print("6. Show call cost")
				print("7. Call cost settings")
				print("8. Prepaid credit")
				print("9. Back")
				fourth_choice = int(input("Enter 9 to quit: "))
				match fourth_choice:
					case 1:
						under_fourth1 = 0
						while under_fourth1 != 2:
							print("1. Missed calls")
							print("2. Back")
							under_fourth1 = int(input("Enter 2 to quit: "))
							if under_fourth1 == 2:
								break
					case 2:
						under_fourth2 = 0
						while under_fourth2 != 3:
							print("2. Received calls")
							print("3. Back")
							under_fourth2 = int(input("Enter 3 to quit: "))
							if under_fourth2 == 3:
								break
					case 3:
						under_fourth3 = 0
						while under_fourth3 != 4:
							print("3. Dialled numbers")
							print("4. Back")
							under_fourth3 = int(input("Enter 4 to quit: "))
							if under_fourth3 ==4:
								break
					case 4:
						under_fourth4 = 0
						while under_fourth4 != 5:
							print("4. Erase recent call lists")
							print("5. Back")
							under_fourth4 = int(input("Enter 5 to quit: "))
							if under_fourth4 == 5:
								break
					case 5:
						under_fourth5 = 0
						while under_fourth5 != 6:
							print("5. Show call duration")
							print("1. Last call duration")
							print("2. All call's duration")
							print("3. Received call's duration")
							print("4. Dialled call's duration")
							print("5. Clear timers")
							print("6. Back")
							under_fourth5 = int(input("Enter 6 to quit: "))
							if under_fourth5 == 6:
								break
							match under_fourth5:
								case 1:
									under_fourth51 = 0
									while under_fourth51 != 2:
										print("1. Last call duration")
										print("2. Back")
										under_fourth51 = int(input("Enter 2 to quit: "))
										if under_fourth51 == 2:	
											break
								case 2:
								
									under_fourth52 = 0
									while under_fourth52 != 2:
										print("1. All call's duration")
										print("2. Back")
										under_fourth52 = int(input("Enter 2 to quit: "))
										if under_fourth52 == 2:	
											break
								case 3:
								
									under_fourth53 = 0
									while under_fourth53 != 2:
										print("1. Received call's duration")
										print("2. Back")
										under_fourth53 = int(input("Enter 2 to quit: "))
										if under_fourth53 == 2:	
											break
								case 4:
								
									under_fourth54 = 0
									while under_fourth54 != 2:
										print("1. Dialled call's duration")
										print("2. Back")
										under_fourth54 = int(input("Enter 2 to quit: "))
										if under_fourth54 == 2:	
											break
								case 5:
								
									under_fourth55 = 0
									while under_fourth55 != 2:
										print("1. Clear timers")
										print("2. Back")
										under_fourth55 = int(input("Enter 2 to quit: "))
										if under_fourth55 == 2:	
											break					
					case 6:
						under_fourth6 = 0
						while under_fourth6 != 7:
							print("6. Show call cost")
							print("1. Last call's cost")
							print("2. All call's cost")
							print("3. Clear counters")
							print("7. Back")
							under_fourth6 = int(input("Enter 7 to quit: "))
							if under_fourth6 == 7:
								break
							match under_fourth6:
								case 1:
									under_fourth61 = 0
									while under_fourth61 != 2:
										print("1. Last call's cost")
										print("2. Back")
										under_fourth61 = int(input("Enter 2 to quit: "))
										if under_fourth61 == 2:
											break
								case 2:	
									under_fourth62 = 0
									while under_fourth62 != 2:
										print("2.All call's cost")
										print("2. Back")
										under_fourth62 = int(input("Enter 2 to quit: "))
										if under_fourth62 == 2:
											break
								case 3:
									under_fourth63 = 0
									while under_fourth63 != 2:
										print("3. Clear counters")
										print("2. Back")
										under_fourth63 = int(input("Enter 2 to quit: "))
										if under_fourth63 == 2:
											break
					case 7:
						under_fourth7 = 0
						while under_fourth7 != 8:
							print("7. Cost call settings")
							print("1. Call cost limit")
							print("2. Show cost in")
							print("8. Back")
							under_fourth7 = int(input("Enter 8 to quit: "))
							if under_fourth7 == 8:
								break
							match under_fourth7:
								case 1:
									under_fourth71 = 0
									while under_fourth71 != 2:
										print("1. Call cost limit")
										print("2. Back")
										under_fourth71 = int(input("Enter 2 to quit: "))
										if under_fourth71 == 2:
											break
								case 2:
									under_fourth72 = 0
									while under_fourth72 != 2:
										print("1. Show cost in")
										print("2. Back")
										under_fourth72 = int(input("Enter 2 to quit: "))
										if under_fourth72 == 2:
											break
					case 8:
						under_fourth8 = 0
						while under_fourth8 != 9:
							print("8. Prepaid credit")
						break
		case 5:
			print("====Tones====")
			print("1. Ringing tone")
			print("2. Ringing volume")
			print("3. Incoming call alert")
			print("4. Composer")
			print("5. Message alert tone")
			print("6. Keypad tones")
			print("7. Warning and game tones")
			print("8. Vibrating alert")
			print("9. Screen saver")
			match fifth_choice:
				case 1:
					print("1. Ringing Tone")
				case 2:
					print("1. Ringing volume")
				case 3:
					print("1. Incoming call alert")
				case 4:
					print("1. Composer")
				case 5:
					print("1. Message alert tone")
				case 6:
					print("1. Keypad tones")
				case 7:
					print("1. Warning and game tones")
				case 8:
					print("1. Vibrating alert")
				case 9:
					print("1. Screen saver")
					break
		case 6:
			print("====Settings====")
			print("1. Call settings")
			print("2. Phone settings")
			print("3. Security settings")
			print("4. Rsetore factory settings")
	
				match sixth_choice :
					case 1:
						print("Call settings")
						print("1. Automatic redial")
						print("2. Speed dialing")
						print("3. Call waiting action")
						print("4. Own number sending")
						print("5. Phone line in use")
						print("6. Automatic answer")
						match sixth_choice1 :
							case 1:
								print("1. Automatic redial")
							case 2:
								print("1. Speed dialing")
							case 3:
								print("1. Call waiting options")
							case 4:
								print("1. Own number sending")
							case 5:
								print("1. Phone line in use")
							case 6:
								print("1. Automatic answer")						
					case 2:
						print("Phone settings")
						print("1. Language")
						print("2. Cell info display")
						print("3. Welcome note")
						print("4. Network selection")
						print("5. Lights")
						print("6. Condirm SIM service actions")
						match sixth_choice2 :
							case 1:
								print("1. Language")
							case 2:
								print("1. Cell info display")
							case 3:
								print("1. Welcome Note")
							case 4:
								print("1. Network selection")
							case 5:
								print("1. Lights")
							case 6:																				print("1. Confirm SIM service actions")
								break
					case 3:
						print("Security settings")
						print("1. PIN code request")
						print("2. Call barring service")
						print("3. Fixed dialing")
						print("4. Closed user group")
						print("5. Phone security")
						print("6. Change access codes")
						match sixth_choice3 :
								case 1:
									print("1. PIN code request")
								case 2:
									print("1. Call barring service")
								case 3:
									print("1. Fixed dialing")
								case 4:
									print("1. Closed user group")
								case 5:
									print("1. Phone security")
								case 6:
									print("1. Change access code")	
								break
					case 4:
						print("Rsetore factory settings")
							break
		case 7:
			print("1. Call divert")
		case 8:
			print("1. Games")
		case 9:
			print("1. Calculator")
		case 10:
			print("1. Reminders")
		case 11:
			print("====Clock====")
			print("1. Alarm clock")
			print("2. Clock settings")
			print("3. Date settings")
			print("4. Stopwatch")
			print("5. Countdown timer")
			print("6. Auto update of date and time")
			
			match eleventh_choice:
					case 1:
						print("1. Alarm clock")
					case 2:
						print("1. Clock settings")
					case 3:
						print("1. Date settings")
					case 4:
						print("1. Stopwatch")
					case 5:
						print("1. Countdown timer")
					case 6:
						print("1. Auto update of date and time")
		case 12:
			print("1. Profiles")
		case 13:
			print("1. SIM services")
		case _:
			print("Au revoir!!!")
