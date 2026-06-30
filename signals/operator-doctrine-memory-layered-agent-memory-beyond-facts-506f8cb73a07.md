# Operator-Doctrine Memory: Layered Agent Memory Beyond Facts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-layered-agent-memory-beyond-facts-506f8cb73a07`
Run ID: `operator-doctrine-memory-layered-agent-memory-beyond-facts-506f8cb73a07-20260619T101703368618+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06fb855ec8bb

## What looked useful

Layered doctrine memory achieved 100% accuracy on 16,000 synthetic doctrine-conflict cases versus 25% for flat top-3 mixed retrieval and 0% for fact-only retrieval, while all agents achieved 100% on 4,000 fact-aligned controls. This supports testing doctrine/fact separation as a memory-evaluation dimension beyond factual recall.

## Boundaries and scale limits

Synthetic symbolic tasks only; no LLM calls, no persistent multi-session memory store, no human-labeled operator doctrine, no noisy natural-language rule induction, and no broad deployment validation.

## Claim scope

In a synthetic deterministic benchmark with 20,000 operator-memory cases, explicit doctrine/fact layering resolved doctrine-conflict action choices better than flat lexical retrieval while preserving fact-aligned control accuracy.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and does not validate real agent memory behavior.

## Recommended next action

Run a bounded deepen follow-up using real LLM agents, persistent memory, natural-language doctrine matching, and overlapping/conflicting doctrine rules before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language doctrine memory arbitration in real LLM agents
- Success threshold: Layered memory improves doctrine-conflict accuracy by at least 15 percentage points over flat retrieval with no more than 3 percentage points loss on fact-aligned recall across at least 300 held-out cases.
- Stop condition: Stop if layered memory fails to beat flat retrieval by 5 percentage points on doctrine-conflict accuracy or causes more than 10 percentage points loss on fact-aligned recall in the first 100 held-out cases.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-layered-agent-memory-beyond-facts-506f8cb73a07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
