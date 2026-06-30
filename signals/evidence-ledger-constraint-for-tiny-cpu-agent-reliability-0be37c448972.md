# Evidence-ledger constraint for tiny CPU agent reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-for-tiny-cpu-agent-reliability-0be37c448972`
Run ID: `evidence-ledger-constraint-for-tiny-cpu-agent-reliability-0be37c448972-20260528T133613321418+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c8ad9af5b056

## What looked useful

Ledger reduced unsupported commit rate from 0.552397 baseline mean to 0.123644, mean delta -0.428753 with condition-level 95% CI [-0.491599, -0.365907]. It reduced unsupported commits in 69/72 conditions, tied in 3/72 easy conditions, and was worse in 0/72. Precision when answered improved from 0.479958 to 0.748422, while abstention rose to 0.468322 and all-question accuracy fell by 0.071561.

## Boundaries and scale limits

Synthetic symbolic benchmark only; no real LLM, no real retrieval corpus, no long-horizon tool use, no human task evaluation, and no full-scale serving or training validation. Main run was 72 paired conditions, 10 seeds, 500 episodes per seed-condition, completed in 38.98 seconds on CPU.

## Claim scope

In a seeded synthetic evidence-grounded slot QA benchmark for tiny CPU agents, an evidence-ledger commitment rule reduces unsupported answer commitments under matched noisy retrieval/extraction, at the cost of higher abstention and lower all-question accuracy.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but direct real-agent evidence is required before any publication-grade claim.

## Recommended next action

Run a bounded real tiny-model follow-up using a local small instruction model on evidence-grounded QA/tool tasks with matched ledger/no-ledger prompts and direct unsupported-claim evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-model evidence-ledger reliability check
- Success threshold: Ledger condition reduces unsupported claim rate by at least 30% relative to baseline with no more than a 15 percentage-point absolute drop in task completion/all-question accuracy across the bounded task set.
- Stop condition: Stop as negative if unsupported claim reduction is below 10%, if task completion drops by more than 25 percentage points, or if CPU latency/overhead makes the tiny-agent setting impractical for the tested model.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-for-tiny-cpu-agent-reliability-0be37c448972`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
