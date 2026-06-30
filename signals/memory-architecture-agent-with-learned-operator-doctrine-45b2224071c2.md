# Memory-Architecture Agent with Learned Operator Doctrine

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-architecture-agent-with-learned-operator-doctrine-45b2224071c2`
Run ID: `memory-architecture-agent-with-learned-operator-doctrine-45b2224071c2-20260613T072931308109+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e553faf733bb

## What looked useful

Layered doctrine memory reached 20/20 exact-answer accuracy versus 16/20 for flat retrieval, 15/20 for transcript search, and 0/20 for no memory. The +0.20 layered-vs-flat delta met the predeclared local success threshold by fixing doctrine precedence failures.

## Boundaries and scale limits

Synthetic symbolic tasks only; no LLM calls, no learned operator, no production memory store, no large corpus, and no long-horizon real operator traces.

## Claim scope

On a 20-task deterministic synthetic replay suite, separating operator doctrine records from ordinary episodic facts avoided later-conflicting-fact precedence errors that affected flat retrieval.

## Why it stopped

Scoped synthetic replay supports a mechanism but is proxy-only and insufficient for paper-positive validation of a learned operator doctrine.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded held-out replay with paraphrased tasks and a learned or model-mediated doctrine extractor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out paraphrased replay for learned doctrine extraction
- Success threshold: Layered doctrine memory accuracy >= 0.85 and at least +0.15 over flat retrieval overall, with at least +0.25 over flat retrieval on doctrine-precedence conflicts.
- Stop condition: Stop if layered doctrine memory is below 0.75 overall accuracy, fails to beat flat retrieval by 0.10 overall, or doctrine extraction errors dominate more than half of doctrine-precedence failures.

## Evidence references

- Artifact root: `<local-path>/projects/memory-architecture-agent-with-learned-operator-doctrine-45b2224071c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
