# Suffix-tree vs tiny local draft for speculative decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-vs-tiny-local-draft-for-speculative-decoding-on-gb10-8ec8f2368a50`
Run ID: `suffix-tree-vs-tiny-local-draft-for-speculative-decoding-on-gb10-8ec8f2368a50-20260613T172501961880+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d25e02f83924

## What looked useful

Suffix lookup had 91.7% proposal coverage and 80.7% acceptance on repeat-heavy states with about 0.36x target-greedy accepted-token cost, but only 8.3% coverage on natural states. The tiny Pythia-70m draft proposed everywhere but had 39.6% overall acceptance and about 1.24x target-greedy accepted-token cost.

## Boundaries and scale limits

Small local models, 72 prompt states, handcrafted natural/repeat prompt suite, 4-token drafts, no full production speculative loop, no batched serving, no 7B+ target, and no draft model trained specifically to match the target.

## Claim scope

On GB10 with cached EleutherAI/pythia-410m as target and EleutherAI/pythia-70m as tiny draft, a CPU suffix lookup proposer is useful for repeat-heavy prompt states but not for natural prompt states; the tested tiny draft does not beat target-greedy accepted-token cost in this bounded proxy.

## Why it stopped

Bounded proxy evidence is mixed: suffix lookup is promising only for repeat-heavy contexts, while the tested tiny local draft is net negative versus target greedy; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a full cached speculative loop on repeat-heavy code/RAG workloads and a target-matched draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full cached speculative loop for suffix lookup on repeat-heavy code and RAG contexts
- Success threshold: Suffix lookup achieves at least 1.5x end-to-end generated-token throughput over target greedy on repeat-heavy workloads, with no more than 5% regression when disabled or falling back on natural workloads.
- Stop condition: Stop if full-loop suffix lookup is below 1.2x throughput on repeat-heavy prompts or causes more than 5% regression on natural prompts after fallback gating.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-vs-tiny-local-draft-for-speculative-decoding-on-gb10-8ec8f2368a50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
