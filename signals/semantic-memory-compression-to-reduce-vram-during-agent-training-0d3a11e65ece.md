# Semantic memory compression to reduce VRAM during agent training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-memory-compression-to-reduce-vram-during-agent-training-0d3a11e65ece`
Run ID: `semantic-memory-compression-to-reduce-vram-during-agent-training-0d3a11e65ece-20260610T082636079377+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b85f706b1f3e

## What looked useful

Full context and semantic-compressed modes both reached 100% eval accuracy, while recency-only stayed near chance at 6.3%. At batch 64, full 512-token training peaked at 1003.3 MiB CUDA allocation versus 190.4 MiB for 65-token semantic compression, an 81.0% reduction. A one-step scaling probe showed full-context allocation rising from 299.5 MiB at 128 tokens to 1451.9 MiB at 768 tokens, while compressed stayed about 185 MiB.

## Boundaries and scale limits

The semantic memory token was an oracle/informative compressed state in a toy delayed-key task; this does not validate a learned compressor, real agent trajectories, RL credit assignment, GPT-2-scale models, or long-horizon training stability.

## Claim scope

On a synthetic delayed-memory transformer training task, replacing a 512-token history with a 65-token recent-plus-semantic representation preserved task accuracy while reducing measured peak CUDA allocation.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports the memory-saving mechanism only under an oracle synthetic compression proxy, not as direct/full validation of learned semantic memory during real agent training.

## Recommended next action

Run a bounded deepen test with a learned segment compressor on recorded or simulated agent trajectories, requiring retained return/accuracy versus full memory and measured CUDA savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned semantic compressor on delayed-memory agent trajectories
- Success threshold: Learned compression uses at least 75% less peak CUDA allocation than full context at matched batch/model size while retaining at least 95% of full-context held-out performance across three seeds.
- Stop condition: Stop if learned-compressed performance is within 10% of recency-only or loses more than 10 percentage points versus full context after a matched bounded training budget.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-memory-compression-to-reduce-vram-during-agent-training-0d3a11e65ece`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
