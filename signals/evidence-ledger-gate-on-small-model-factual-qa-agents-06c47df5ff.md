# Evidence ledger gate on small-model factual QA agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gate-on-small-model-factual-qa-agents-06c47df5ff`
Run ID: `evidence-ledger-gate-on-small-model-factual-qa-agents-06c47df5ff-20260603T232431027075+0000`

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

- Parent run decision: Evidence Ledger Reduces Hallucination in Tiny Agents: enoch://control-plane/projects/evidence-ledger-reduces-hallucination-in-tiny-agents-d99cb8d44249/runs/evidence-ledger-reduces-hallucination-in-tiny-agents-d99cb8d44249-20260603T195533993078+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c067134b618a

## What looked useful

Across three seeds, baseline unsupported non-abstained rate averaged 0.413 and gated unsupported non-abstained rate was 0.000; gated accuracy averaged 0.808 versus baseline 0.550, with mean gated coverage 0.588. The gate acted mainly by forced abstention rather than repair.

## Boundaries and scale limits

Synthetic controlled facts only; lexical support rule only; no open-domain retrieval, natural QA benchmark, semantic entailment judge, multi-hop reasoning, adversarial evidence, or production multi-turn agents were tested.

## Claim scope

In a controlled fictional factual-QA task with google/flan-t5-small and supplied evidence snippets, an external evidence-ledger gate requiring a cited line to contain both the question subject and answer reduced unsupported non-abstained answers to zero across three 80-item seeds while preserving at least 95.6% of baseline correct answerable answers.

## Why it stopped

Tier 1 controlled direct test completed and supports the mechanism, but the result is synthetic and bounded, so it is no-paper useful signal rather than paper-positive evidence.

## Recommended next action

Run a deepen follow-up on a real small factual QA benchmark with held-out contexts and ablations for citation-only prompting, lexical ledger gate, and semantic entailment gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-context benchmark ablation for evidence-ledger gates on small factual QA agents
- Success threshold: At least 35% relative reduction in unsupported non-abstained answers versus citation-only prompting, with at least 80% retention of baseline answerable accuracy and no more than 25 percentage-point absolute coverage loss versus citation-only prompting.
- Stop condition: Stop if the gate fails to reduce unsupported non-abstained answers by 20% on the first real benchmark seed or if answerable-accuracy retention falls below 65%, because the controlled synthetic effect would not transfer enough to justify scaling.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gate-on-small-model-factual-qa-agents-06c47df5ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
