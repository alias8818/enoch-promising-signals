# LLM answerer validation for layered doctrine memory replay conflicts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-answerer-validation-for-layered-doctrine-memory-replay-64062c44a4`
Run ID: `llm-answerer-validation-for-layered-doctrine-memory-replay-64062c44a4-20260621T142007881573+0000`

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

- Parent run decision: LLM-in-the-loop layered doctrine memory replay benchmark: enoch://control-plane/projects/llm-in-the-loop-layered-doctrine-memory-replay-benchmark-dc52aff568/runs/llm-in-the-loop-layered-doctrine-memory-replay-benchmark-dc52aff568-20260621T134821977045+0000
- Parent run decision: Agent memory architecture: layered operator-doctrine vs flat retrieval: enoch://control-plane/projects/agent-memory-architecture-layered-operator-doctrine-vs-flat-retrieval-3531b9e27832/runs/agent-memory-architecture-layered-operator-doctrine-vs-flat-retrieval-3531b9e27832-20260621T125842067808+0000

## What looked useful

Layered doctrine memory reached 1.00 accuracy and 0.00 conflict violation rate. Flat retrieval and transcript search reached 0.75 accuracy with 0.25 conflict violation rate. Ablations showed scope binding, temporal ordering, and precedence are each necessary in this controlled setting.

## Boundaries and scale limits

Synthetic template-generated replay tasks; deterministic extractive answerer rather than a real LLM; no naturalistic transcript corpus, human gold labels, production memory traces, or model variance tests.

## Claim scope

In a 600-case fixed-seed synthetic replay suite with a constrained extractive answerer, layered doctrine memory resolved temporal, precedence, scope, and combined conflicts better than no-memory, transcript-search, and flat-retrieval baselines, and each targeted ablation failed on its intended conflict class.

## Why it stopped

Tier 2 local mechanism evidence was produced, but the run remains no-paper because it used synthetic tasks and a constrained extractive answerer instead of real LLM answer generation.

## Recommended next action

Run the same fixed replay suite and ablations with a frozen small instruction model answerer, preserving seeds and measuring exact answer accuracy plus conflict violation rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen small-LLM answerer validation for layered doctrine replay conflicts
- Success threshold: Layered doctrine memory improves accuracy by at least 0.15 over flat_retrieval and reduces conflict violation rate by at least 50% across at least 4 of 5 seeds, with no ablation matching the full layered strategy.
- Stop condition: Stop if layered_doctrine_memory fails to beat flat_retrieval by 0.05 accuracy on two or more seeds or if conflict violations remain within 10% relative of flat_retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/llm-answerer-validation-for-layered-doctrine-memory-replay-64062c44a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
