# Evidence-Ledger Agent with Compressed Episodic Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-with-compressed-episodic-anchors-8f015817ceba`
Run ID: `evidence-ledger-agent-with-compressed-episodic-anchors-8f015817ceba-20260526T063251094295+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2df4cd4f2a67

## What looked useful

Minimal evidence-linked anchors reached 1.000 mean joint answer/citation accuracy at 256-2048 bytes in the 100-fact sweep and 0.993-1.000 in the harder 120-fact/20-distractor sweep, while raw BM25 stayed at 0.006-0.958 in the first sweep and 0.002-0.040 in the stress sweep; summary-only memory had nonzero answer accuracy but 0.000 citation accuracy.

## Boundaries and scale limits

No LLM agent loop, real task corpus, vector retrieval baseline, noisy extraction, conflicting updates, or multi-hop evidence was tested. Results are proxy evidence for the memory representation, not publication-grade validation of a deployed evidence-ledger agent.

## Claim scope

In a deterministic synthetic episodic-QA proxy with fixed context byte budgets, compressed minimal anchors that preserve evidence ids achieved near-perfect answer-and-citation retrieval across tested seeds and distractor densities, outperforming raw BM25 retrieval and non-ledger summaries under tight budgets.

## Why it stopped

Closed as a no-paper useful signal because the evidence is synthetic and deterministic; it supports the anchor mechanism but does not directly validate a full evidence-ledger agent.

## Recommended next action

Run a bounded real-agent follow-up that plugs minimal evidence anchors into an LLM episodic QA loop and evaluates citation-checked accuracy against raw retrieval and summary baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM agent validation of minimal evidence-ledger anchors on episodic QA
- Success threshold: At least 15 percentage points higher joint answer-and-citation accuracy than raw retrieval at matched context budget on two or more held-out episodic QA settings, without increasing hallucinated evidence ids.
- Stop condition: Stop if anchors fail to beat raw retrieval by 5 percentage points in joint accuracy at matched budget on the first held-out LLM-agent benchmark or if citation hallucination exceeds the raw retrieval baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-with-compressed-episodic-anchors-8f015817ceba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
