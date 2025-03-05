import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogTitle } from "@/components/ui/dialog";

const skills = [
  { id: 1, skill: "Python Programming", user: "Alice" },
  { id: 2, skill: "Guitar Lessons", user: "Bob" },
  { id: 3, skill: "Data Analysis", user: "Charlie" },
  { id: 4, skill: "Digital Marketing", user: "Diana" },
];

export default function SkillSwap() {
  const [search, setSearch] = useState("");
  const [selectedSkill, setSelectedSkill] = useState(null);

  const filteredSkills = skills.filter((s) =>
    s.skill.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold text-center mb-6">SkillSwap Platform</h1>
      <Input
        placeholder="Search for a skill..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="mb-4"
      />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredSkills.map((s) => (
          <Card key={s.id} onClick={() => setSelectedSkill(s)} className="cursor-pointer hover:shadow-lg">
            <CardContent className="p-4">
              <h2 className="text-xl font-semibold">{s.skill}</h2>
              <p className="text-gray-600">Offered by {s.user}</p>
            </CardContent>
          </Card>
        ))}
      </div>
      <Dialog open={!!selectedSkill} onOpenChange={() => setSelectedSkill(null)}>
        <DialogContent>
          <DialogTitle>Request a Skill Swap</DialogTitle>
          {selectedSkill && (
            <div className="p-4">
              <p className="text-lg">Learn {selectedSkill.skill} from {selectedSkill.user}</p>
              <Button className="mt-4">Request Swap</Button>
            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
