# Strip Intercom bot noise from a get_conversation payload and print the
# human-readable thread: subject, sender, attributes, SLA, opening message
# and every human reply in order.
#
# Usage:  jq -rf extract.jq conversation.json

def clean: gsub("<[^>]*>";" ") | gsub("&nbsp;";" ") | gsub("&amp;";"&")
         | gsub("&#39;";"'") | gsub("&quot;";"\"") | gsub("&#x27;";"'")
         | gsub("[ \t]+";" ");

"### CONV \(.id)  [\(.created_at|todate)]  state=\(.state)",
"SUBJECT: \((.source.subject//"")|clean)",
"FROM:    \(.source.author.name//"?") <\(.source.author.email//"?")> (\(.source.author.type))",
"ATTRS:   user=\(.custom_attributes["Type of user"]//"-") provider=\(.custom_attributes["Provider"]//"-") topic=\(.custom_attributes["PL:Topic"]//.custom_attributes["BenOps: Topic"]//"-") fin=\(.ai_agent_participated)",
"SLA:     \(.sla_applied.sla_name//"-") => \(.sla_applied.sla_status//"-")",
"",
"--- OPENING ---",
((.source.body//"")|clean),
"",
"--- REPLIES ---",
(
  [.conversation_parts.conversation_parts[]
   | select(.part_type=="comment" or .part_type=="note")
   | select(.body != null and .body != "")]
  | if length==0 then "(none)" else
    (.[] | ">>> [\(.created_at|todate)] \(.author.name) <\(.author.email//"-")> (\(.author.type)) \(.part_type)\n\((.body)|clean)\n")
  end
)
