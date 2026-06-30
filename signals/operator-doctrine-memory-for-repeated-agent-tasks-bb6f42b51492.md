# Operator-doctrine memory for repeated agent tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-for-repeated-agent-tasks-bb6f42b51492`
Run ID: `operator-doctrine-memory-for-repeated-agent-tasks-bb6f42b51492-20260628T170621919637+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/27a841f3269d

## What looked useful

Compact operator-doctrine memory reduced repeated errors in synthetic repeated tasks while using far fewer rules than exact episodic storage. The key tradeoff is memory efficiency versus a noisier, more detailed doctrine memory that can be slightly more accurate in richer distractor settings.

## Boundaries and scale limits

Proxy-only CPU benchmark: no real LLM agents, no natural-language doctrine extraction, no real repositories, no human scoring, and no long-horizon production task drift. Main sweep was 100 seeds x 300 synthetic episodes; robustness grid was 9 settings with 50 seeds each.

## Claim scope

Synthetic sequential repeated-task benchmark with latent operational motifs, distractor features, and observed action outcomes. Compact motif-level doctrine improved accuracy and memory efficiency versus no memory and exact episodic memory, but was not always the top-accuracy policy versus a larger noisy doctrine control.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not direct/full validation of repeated real-agent tasks, and the compressed doctrine policy does not dominate the larger noisy doctrine control on accuracy.

## Recommended next action

Run a bounded deepen follow-up using real LLM-driven repeated coding or operations tasks with textual doctrine extraction and held-out task families; stop this run as no-paper proxy evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM agent doctrine memory on held-out repeated coding tasks
- Success threshold: Compact doctrine improves held-out success by at least 10 percentage points over no memory and is within 3 percentage points of detailed doctrine while using at least 50% fewer retrieved tokens or memory entries.
- Stop condition: Stop if compact doctrine fails to beat no memory by 5 percentage points on held-out tasks or requires more retrieved context than exact episodic retrieval to match its success rate.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-for-repeated-agent-tasks-bb6f42b51492`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
