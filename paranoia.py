import Banners
import os

import Options.main_opt

stop = int(1)
while stop == 1:
    try:
        print(Banners.main_ban.banner_main)

        domain = str(input("Digite a url: "))
        block = int(input("Digite o bloco que deseja usar: "))

        match block:
            case 1:
                while stop == 1:
                    import Enumeration

                    os.system("clear")
                    print(Banners.main_ban.banner_enum)

                    tool = int(input("Informe o número da ferramenta: "))
                    os.system("clear")

                    match tool:
                        case 1:
                            Enumeration.main_enum.gf(domain)
                        case 2:
                            Enumeration.main_enum.arjun(domain)
                        case 3:
                            Enumeration.main_enum.unfurl(domain)
                        case 4:
                            Enumeration.main_enum.paramspider(domain)
                        case 5:
                            Enumeration.main_enum.subjs(domain)
                        case 6:
                            Enumeration.main_enum.anti_burl()
                        case 7:
                            Enumeration.main_enum.amass(domain)
                        case 8:
                            Enumeration.main_enum.metabigor(domain)

                    num = int(input("Deseja continuar?[0/1] "))
                    os.system("clear")
                    stop += num

                    if stop:
                        pass
                    else:
                        break

            case 2:
                while stop == 1:
                    import Information

                    os.system("clear")
                    print(Banners.main_ban.banner_info)

                    tool = int(input("Informe o número da ferramenta: "))
                    os.system("clear")

                    match tool:
                        case 1:
                            Information.main_info.host(domain)
                        case 2:
                            Information.main_info.whois(domain)
                        case 3:
                            Information.main_info.censys(domain)
                        case 4:
                            Information.main_info.dnsenum(domain)
                        case 5:
                            Information.main_info.dnsrecon(domain)
                        case 6:
                            Information.main_info.nmap(domain)
                        case 7:
                            Information.main_info.waf(domain)

                    num = int(input("Deseja continuar?[0/1] "))
                    os.system("clear")
                    stop += num

                    if stop:
                        pass
                    else:
                        break

            case 3:
                while stop == 1:
                    import Scanners

                    os.system("clear")
                    print(Banners.main_ban.banner_scan)

                    tool = int(input("Informe o número da ferramenta: "))
                    os.system("clear")

                    match tool:
                        case 1:
                            Scanners.main_scan.jsql()
                        case 2:
                            Scanners.main_scan.dotdotpwn(domain)
                        case 3:
                            Scanners.main_scan.search()
                        case 4:
                            Scanners.main_scan.wp_scan()
                        case 5:
                            Scanners.main_scan.burp_suit()

                    num = int(input("Deseja continuar?[0/1] "))
                    os.system("clear")
                    stop += num

                    if stop:
                        pass
                    else:
                        break

            case 4:
                while stop == 1:
                    import Structure

                    os.system("clear")
                    print(Banners.main_ban.banner_str)


                    tool = int(input("Informe o número da ferramenta: "))
                    os.system("clear")

                    match tool:
                        case 1:
                            Structure.main_struct.xargs()
                        case 2:
                            Structure.main_struct.nuclei()
                        case 3:
                            Structure.main_struct.dalfox()
                        case 4:
                            Structure.main_struct.katana(domain)

                    num = int(input("Deseja continuar?[0/1] "))
                    os.system("cear")
                    stop += num

                    if stop:
                        pass
                    else:
                        break


            case 5:
                while stop == 1:
                    import Subdomain

                    os.system("clear")
                    print(Banners.main_ban.banner_sub)


                    tool = int(input("Informe o número da ferramenta: "))
                    os.system("clear")

                    match tool:
                        case 1:
                            Subdomain.main_sub.kitterunner(domain)
                        case 2:
                            Subdomain.main_sub.git_api(domain)
                        case 3:
                            Subdomain.main_sub.git_dorker(domain)
                        case 4:
                            Subdomain.main_sub.wfuzz(domain)
                        case 5:
                            Subdomain.main_sub.ffuf(domain)
                        case 6:
                            Subdomain.main_sub.feroxbuster(domain)
                        case 7:
                            Subdomain.main_sub.gauplus(domain)
                        case 8:
                            Subdomain.main_sub.waymore(domain)
                        case 9:
                            Subdomain.main_sub.httpx(domain)
                        case 10:
                            Subdomain.main_sub.httprobe()
                        case 11:
                            Subdomain.main_sub.aquatone()

                    num = int(input("Deseja continuar?[0/1] "))
                    os.system("clear")
                    stop += num

                    if stop:
                        pass
                    else:
                        break

            case 6:
                while stop == 1:
                    import Options

                    os.system("clear")
                    print(Banners.main_ban.banner_opt)

                    tool = int(input("Número da opção: "))
                    os.system("clear")

                    match tool:
                        case 1:
                            print(Options.main_opt.man)
                        case 2:
                            print(Options.main_opt.infos)
                        case 3:
                            Options.main_opt.other(domain)
                        case 4:
                            print(Options.main_opt.report)
                        case 5:
                            Options.main_opt.hacker_help()
                        case 6:
                            print(Options.main_opt.content)
                        case 7:
                            Options.main_opt.options_install_tools()

                    num = int(input("Deseja continuar?[0/1] "))
                    os.system("clear")
                    stop += num

                    if stop:
                        pass
                    else:
                        break
    except:
        print("\nAlgo deu errado.")
        num = int(input("Deseja continuar?[0/1] "))
        stop += num

        if stop:
            os.system("clear")
            pass
        else:
            break
