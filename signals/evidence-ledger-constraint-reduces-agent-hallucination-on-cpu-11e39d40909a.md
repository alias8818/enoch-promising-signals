# Evidence-Ledger Constraint Reduces Agent Hallucination on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constraint-reduces-agent-hallucination-on-cpu-11e39d40909a`
Run ID: `evidence-ledger-constraint-reduces-agent-hallucination-on-cpu-11e39d40909a-20260527T020213426331+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/42851e3fbff3

## What looked useful

Across 270,000 requested claim slots, baseline unsupported published claim rate was 0.5133 and ledger unsupported published claim rate was 0.0000. With 10% false target evidence, ledger incorrect published claim rate was still 0.1645, showing the constraint reduces unsupported claims but does not guarantee truth.

## Boundaries and scale limits

No real LLM, no natural-language entailment, no retrieval corpus, no citation gaming, and no multi-hop reasoning were tested. The contaminated-evidence condition showed that false facts inside the ledger still produce incorrect ledger-backed claims.

## Claim scope

In a CPU-local synthetic control where factual claim proposals are held fixed and evidence is represented as exact entity-attribute-value tuples, an evidence-ledger publication gate eliminated claims absent from retrieved evidence across 18 tested conditions.

## Why it stopped

Proxy synthetic evidence supports the mechanism but is not direct/full validation of real agent hallucination reduction.

## Recommended next action

Run a bounded direct LLM-agent deepen test on a small fact-verification or QA dataset with retrieved passages and metrics separating unsupported, wrong-but-cited, abstained, and correct supported claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small LLM Evidence-Ledger QA Hallucination Test
- Success threshold: At least 50% relative reduction in unsupported final claims versus baseline, no increase in wrong-but-cited claim rate, and no more than 25% relative loss in correct supported claims.
- Stop condition: Stop if the ledger constraint fails to reduce unsupported claims by 25% in the first 100 evaluated claim slots or if evaluator reliability cannot separate unsupported from wrong-but-cited claims.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constraint-reduces-agent-hallucination-on-cpu-11e39d40909a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
