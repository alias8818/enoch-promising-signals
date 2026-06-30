# Agent Memory Doctrine Learning via Repeated Task Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-memory-doctrine-learning-via-repeated-task-compression-c746522d7cd6`
Run ID: `agent-memory-doctrine-learning-via-repeated-task-compression-c746522d7cd6-20260611T200603084917+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/15286057a376

## What looked useful

Doctrine compression improved over no memory but failed against simpler baselines. Final mean held-out success: no_memory 0.0868, recent_retrieval 0.9593, global_compression 0.8879, doctrine_naive 0.7680, doctrine_contrastive 0.3181. Seed-0 rule recovery was poor: naive precision 0.1818/recall 0.25, contrastive precision 0.1429/recall 0.125.

## Boundaries and scale limits

No real LLM summarization, no live software-agent execution, no human-authored doctrine, and no large-scale or multi-session trace corpus. CPU-only run completed in under 2 seconds; evidence is not publication-grade for real agent memory.

## Claim scope

Synthetic proxy with 80 seeded runs, 160 noisy training episodes per seed, and 500 held-out test episodes per seed. Tested compact doctrine-rule induction from repeated task traces against no-memory, recent-retrieval, and global-compression baselines.

## Why it stopped

Synthetic proxy produced no-paper useful evidence: simple repeated task compression learned some behavior versus no memory but was beaten by recent retrieval and global compression, so the broad doctrine-learning claim is not supported here.

## Recommended next action

Stop this run as a proxy early falsification; any next run should test a causal or LLM-in-the-loop doctrine compressor on real agent traces with retrieval and global-compression controls under matched token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Causal LLM Doctrine Compression on Real Agent Traces
- Success threshold: Doctrine memory improves held-out task success by at least 5 percentage points over both recent retrieval and global compression while using no more memory tokens than the stronger control.
- Stop condition: Stop if doctrine memory fails to beat either control on two independently seeded held-out splits or if exported doctrine precision is below 0.5.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-doctrine-learning-via-repeated-task-compression-c746522d7cd6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
