# Memory-Augmented Cascade Router with Operator Doctrine

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-augmented-cascade-router-with-operator-doctrine-526558030241`
Run ID: `memory-augmented-cascade-router-with-operator-doctrine-526558030241-20260628T080142090167+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1e1b24b469b9

## What looked useful

Memory+doctrine achieved mean utility/request 0.0876 versus -0.3169 doctrine-only, -0.3253 memory-only, -0.5860 stateless, and 0.0562 corrupted-memory doctrine. It won all 40 paired seeds against each control; paired delta versus corrupted memory was +0.0314 utility/request with 95% CI half-width 0.0024.

## Boundaries and scale limits

Synthetic simulator only; no real LLM inference, no production traces, no real operator policies, no measured serving latency, and no GPT-2-small-class or larger baseline. The result supports a mechanism probe, not a deployment or paper claim.

## Claim scope

In a local synthetic cascade-routing benchmark with hidden persistent domain/operator effects, a memory-augmented doctrine-aware router improved utility over stateless, doctrine-only, memory-only, and corrupted-memory controls across 40 paired seeds.

## Why it stopped

No-paper closure: the current evidence is a bounded synthetic useful signal, not direct publication-grade validation of real cascade routing.

## Recommended next action

Run a bounded direct-evidence follow-up using real small/medium/large model outputs or a saved task trace, preserving the same doctrine and memory ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct model-backed cascade routing with persistent memory and doctrine ablations
- Success threshold: Memory+doctrine must improve utility by at least 0.05/request over doctrine-only and memory-only controls, win at least 80% of paired seeds/tasks, and keep high-risk safety violations no worse than doctrine-only.
- Stop condition: Stop if memory+doctrine fails to beat either doctrine-only or memory-only by 0.02 utility/request, or if it increases high-risk safety violations above doctrine-only.

## Evidence references

- Artifact root: `<local-path>/projects/memory-augmented-cascade-router-with-operator-doctrine-526558030241`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
