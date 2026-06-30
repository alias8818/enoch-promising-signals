# Evidence Ledger Gate on Free-Form Assistant Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gate-on-free-form-assistant-claims-c7608973c5`
Run ID: `evidence-ledger-gate-on-free-form-assistant-claims-c7608973c5-20260605T152838920101+0000`

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

- Parent run decision: Evidence Ledger Gate on Real LLM Tool-Use Traces: enoch://control-plane/projects/evidence-ledger-gate-on-real-llm-tool-use-traces-fdb69498ab/runs/evidence-ledger-gate-on-real-llm-tool-use-traces-fdb69498ab-20260605T102953732773+0000
- Parent run decision: Agent Reliability via Evidence Ledger for Tool Use: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-for-tool-use-cf3926f9566e/runs/agent-reliability-via-evidence-ledger-for-tool-use-cf3926f9566e-20260605T054044068601+0000

## What looked useful

Across three fixed seeds, 1,200 answer bundles, and 3,600 total claims, the semantic evidence-ledger gate retained 100% of supported claims and blocked 100% of unsupported claims. No gate and citation-only baselines passed 100% of unsupported claims; lexical overlap blocked unsupported claims but also blocked 100% of paraphrased supported claims. A shuffled-ledger ablation collapsed supported retention to about 0.6% mean.

## Boundaries and scale limits

Synthetic typed facts only; no real LLM generations, open-domain retrieval, human labels, neural NLI verifier, multi-hop evidence, or adversarial natural-language paraphrases. The successful verifier has access to the same schema used to generate the benchmark.

## Claim scope

In a deterministic closed-schema benchmark of paraphrased biography-style assistant claims, an evidence-ledger gate that checks typed facts against the cited evidence blocks unsupported substitutions while retaining supported claims.

## Why it stopped

Medium controlled evidence supports the mechanism but is synthetic and schema-coupled, so it is insufficient for a paper or broad factuality claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should evaluate the same ledger-gate protocol on real generated assistant answers with independent support labels and a verifier not coupled to the data generator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gate on real generated assistant answers
- Success threshold: At least 50% relative reduction in unsupported claim pass rate versus citation-only baseline, supported claim retention of at least 80%, and balanced accuracy at least 0.15 above lexical overlap across fixed seeds.
- Stop condition: Stop if unsupported pass reduction is under 20%, supported retention is under 65%, or verifier/decomposition errors dominate more than half of false decisions on a 100-example audit.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gate-on-free-form-assistant-claims-c7608973c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
